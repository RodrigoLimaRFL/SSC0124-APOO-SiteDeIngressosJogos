from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

#from compra_ingressos_app.models import contaComum, PessoaFisica, movimento
from compra_ingressos_app.models import Usuario

def realizarLogin(request):
    if request.method == "POST":
        cpf = request.POST['cpfPessoa']
        senhaDigitada = request.POST['senhaConta']

        print(cpf)
        usuario = consultarCpfCliente(cpf)

        if(usuario):
            senhaVerdadeira = usuario.senha
            if(senhaDigitada == senhaVerdadeira):
                redirect("teste")
            else:
                redirect("realizarLogin")
        else:
            redirect("realizarLogin")
    else:
        return render(request, "compra_ingressos/login.html")
    
def consultarCpfCliente(cpf):
    cliente = Usuario.objects.get(cpf=cpf) # Retorna o objeto pessoa se for achado

    if(cliente):
       return cliente
    else:
        return False