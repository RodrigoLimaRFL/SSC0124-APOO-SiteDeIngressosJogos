from distutils.archive_util import make_zipfile
from xml.parsers.expat import model
from django.db import models
from django.forms import CharField, Field
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
import datetime

class Clube(models.Model):
    nomeClube = models.CharField(max_length=100)
    divisao = models.CharField(max_length=1)
    cidadeOrigem = models.CharField(max_length=100)

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
    cpf = models.CharField(unique = True, max_length=11) # Usado como id do usuário
    dateNasc = models.DateField()
    telefone = models.CharField(max_length=13) #format (61)992831235
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=255)

    # Métodos da classe

    def registrarUser(self):
        #salvar no banco de dados
        self.save()

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