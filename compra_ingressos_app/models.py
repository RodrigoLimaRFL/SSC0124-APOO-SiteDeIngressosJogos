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

#################################################################################################

class Jogo(models.Model):
    clubeCasa = models.ForeignKey(Clube, on_delete=models.CASCADE)
    clubeFora = models.ForeignKey(Clube, on_delete=models.CASCADE)
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
    def recuperarJogo(clube):
        try:
            jogo = Jogo.objects.get(clubeCasa = clube)
            return jogo
        except ObjectDoesNotExist:
            return False


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
    cpf = models.CharField( unique = True, max_length=11)
    dateNasc = models.DateField()
    telefone = models.CharField(max_length=13) #format (61)992831235
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=255)

    # Métodos da classe

    def registrarUser(self):
        #salvar no banco de dados
        self.save()

############################################################################################

class RegistroCompra(models.Model):
    dataRegistro = models.DateField()
    horaRegistro = models.TimeField()
    jogoCompra = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    precoCompra = models.DecimalField(max_digits=10, decimal_places=2)

    def salvarRegistro(self):
        self.save()







# ****** Definição da classe PessoaFisica
class PessoaFisica(models.Model):
    #lista de atributos com os tipos que deverão ser armazenados no banco
    nomePessoa = models.CharField(max_length=100)
    enderecoPessoa = models.CharField(max_length=300)
    cepPessoa = models.IntegerField( )
    telefonePessoa = models.CharField(max_length=100)
    rendaPessoa = models.FloatField( )
    situacaoPessoa = models.IntegerField(default=1)
    cpfPessoa = models.CharField( unique = True, max_length = 11 )
    rgPessoa = models.CharField(max_length=10)
    dataNascimento = models.DateField( )

    # ********  Métodos da classe ************

    #método para registrar uma nova pessoa no banco
    #pega como parâmetro de entrada o objeto que chamou o método (self)
    def registrarPessoa(self):
        #salva no banco as informações contidas no objeto quem chamou o método (self)
        self.save()
    
    #def validarCpf(self, cpf): #a implementar - to-do
            
    def consultarCpf(cpf):        
        try:
            #consulta no banco, na tabela PessoaFisica. Solicita a obtenção do registro com as informações da pessoa 
            #cujo atributo cpfPessoa seja igua a cpf
            #caso essa pessoa seja encontrada no banco, é retornado um objeto com todos os atributos preenchidos
            #o objeto retornado é alocado à variável local cliente
            cliente = PessoaFisica.objects.get(cpfPessoa=cpf) 
            #print(cliente)
            #retorno do objeto cliente do tipo pessoaFisica
            return cliente
        except ObjectDoesNotExist:
            #print("Cliente com cpf nao existe")
            return False #cpf não existe
        
    def atualizarPessoa(self):
        #salva no banco as informações contidas no objeto quem chamou o método (self)
        self.save()
        return self
    
#################################################################################3       
# ****** Definição da classe contaComum 
class contaComum(models.Model):
    #lista de atributos com os tipos que deverão ser armazenados no banco
    idCliente = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE)  # relacionamento entre classes: 1 pessoa Fisica tem 1,* contas
    numeroConta = models.IntegerField(unique=True)
    aberturaConta = models.DateField( )
    fechamentoConta = models.DateField(null=True)
    situacaoConta = models.IntegerField() # 1, 0
    senhaConta = models.CharField(max_length=30)
    saldoConta = models.IntegerField(default=0)

    # ********  Métodos da classe ************

    def abrirConta(self):
        #salva no banco as informações contidas no objeto quem chamou o método (self)
        self.save()
        
    def consultarConta(numeroConta):
        try:
            #consulta no banco, na tabela contaComum. Solicita a obtenção do registro com as informações da conta 
            #cujo atributo numeroConta seja igua ao parâmetro de entrada do método: numeroConta
            #caso essa conta seja encontrada no banco, é retornado um objeto com todos os atributos preenchidos
            #o objeto retornado é alocado à variável local conta
            conta = contaComum.objects.get(numeroConta=numeroConta)
            #print(conta)
            #retorna o objeto encontrado no banco
            return conta
        except ObjectDoesNotExist:
            #print("Conta não existe")
            return False #conta com esse numero não existe
    
    def emitirSaldo(numeroConta):
        try:
            conta = contaComum.objects.get(numeroConta=numeroConta)
            print(conta)
            return conta.saldoConta
        
        except ObjectDoesNotExist:
            print("Conta não existe")
            return False #cpf não existe
        
    def atualizarSaldo(self,valor):
        self.saldoConta = self.saldoConta + valor
        self.save()
        return True
    
    def emitirCartao(self):
        # a ser implementado
        return True


#################################################################################3       
# ****** Definição da classe movimento
class movimento(models.Model):
    #lista de atributos com os tipos que deverão ser armazenados no banco
    idConta = models.ForeignKey(contaComum, on_delete=models.CASCADE)  # relacionamento entre classes: 1 conta tem 1,* movimentos
    tipoMovimento = models.IntegerField() # 1, 2, 3
    dataMovimento = models.DateTimeField(default=datetime.datetime.now())
    valorMovimento = models.FloatField()

    # ********  Métodos da classe ************

    def registrarMovimento(self):
        self.save()
        return True

    #def consultarMovimento():
