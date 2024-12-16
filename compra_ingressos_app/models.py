from distutils.archive_util import make_zipfile
from xml.parsers.expat import model
from django.db import models
from django.forms import CharField, Field
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import datetime

class Clube(models.Model):
    nomeClube = models.CharField(max_length=100)
    divisao = models.CharField(max_length=1)
    cidadeOrigem = models.CharField(max_length=100)

    def __str__ (self):
        return self.nomeClube

    # Métodos da classe

    def registrarClube(self):
        #salvar no banco de dados
        self.save()

    @staticmethod
    def recuperarClube(nomeDoClube):
        try:
            clube = Clube.objects.get(nomeClube = nomeDoClube)
            return clube
        except ObjectDoesNotExist:
            return False
        
    @staticmethod
    def doesClubeExist(nomeDoClube):
        try:
            clube = Clube.objects.get(nomeClube = nomeDoClube)
            return True
        except ObjectDoesNotExist:
            return False

#################################################################################################

class Jogo(models.Model):
    clubeCasa = models.ForeignKey(
        Clube,
        on_delete=models.CASCADE,
        related_name='mandante'
        )
    clubeFora = models.ForeignKey(
        Clube,
        on_delete=models.CASCADE,
        related_name='visitante')
    data = models.DateField()
    hora = models.TimeField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estadio = models.CharField(max_length = 100)
    numero_cadeiras = models.IntegerField()

    # Métodos da classe

    def evitarRepeticao(self):
        if self.clubeCasa == self.clubeFora:
            raise ValidationError("Clube da casa e de fora não podem ser iguais.")

    def registrarJogo(self):
        self.evitarRepeticao()
        #salvar no banco de dados
        self.save()

    @staticmethod
    def recuperarID(id):
        try:
            jogo = Jogo.objects.get(id = id)
            return jogo
        except ObjectDoesNotExist:
            return False
        
##############################################################################################

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(unique=True, max_length=11)  # Usado como id do usuário
    dateNasc = models.DateField()
    telefone = models.CharField(max_length=13)  # format (61)992831235
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=255)
    tipoUsuario = models.IntegerField(default=0)  # 0 = usuario comum, 1 = gerente de clube

    # Métodos da classe
    def registrarUser(self):
        """Salva o usuário no banco de dados com senha criptografada."""
        self.senha = make_password(self.senha)  # Criptografa a senha
        self.save()

    @staticmethod
    def autenticar(cpf, senha):
        """
        Verifica se o CPF e a senha fornecidos são válidos.
        Retorna o usuário se as credenciais forem válidas, caso contrário, retorna False.
        """
        try:
            usuario = Usuario.objects.get(cpf=cpf)
            if check_password(senha, usuario.senha):  # Verifica a senha criptografada
                return usuario
            else:
                return False
        except Usuario.DoesNotExist:
            return False

    def consultarCPF(cpf):
        try:
            usuario = Usuario.objects.get(cpf = cpf)
            return usuario
        except ObjectDoesNotExist:
            return False

############################################################################################

class RegistroCompra(models.Model):
    dataRegistro = models.DateField()
    horaRegistro = models.TimeField()
    jogoCompra = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    precoCompra = models.DecimalField(max_digits=10, decimal_places=2)

    def salvarRegistro(self):
        self.save()