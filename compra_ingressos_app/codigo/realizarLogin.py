from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

from compra_ingressos_app.models import contaComum, PessoaFisica, movimento

def realizarLogin(request):
    if request.method == "POST":
        cpf = request.POST['cpfPessoa']
        senha = request.POST['senha']

        print(cpf)
        usuario = consultarCpfCliente(cpf)

        if(usuario):
            if(senha == usuario.GetSenha()):
                redirect("realizarLogin")
            else:
                redirect("realizarLogin")
        else:
            redirect("realizarLogin")
    else:
        return render(request, "compra_ingressos/login.html")
    
def consultarCpfCliente(cpf):
    cliente = PessoaFisica.consultarCpf(cpf) # Retorna o objeto pessoa se for achado

    if(cliente):
       return cliente
    else:
        return False