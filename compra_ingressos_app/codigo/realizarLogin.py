from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

from compra_ingressos_app.models import Usuario

def realizarLogin(request):
    if request.method == "POST":
        cpf = request.POST['cpfPessoa']
        senhaDigitada = request.POST['senhaConta']

        usuario = Usuario.consultarCPF(cpf)

        if(usuario):
            senhaVerdadeira = usuario.senha
            if(senhaDigitada == senhaVerdadeira):
                mensagem = '''
                    Usuário Logado com sucesso!
                '''
            else:
                mensagem = '''
                    Senha Errada. Tente Novamente!
                '''
        else:
            mensagem = '''
                Usuário Inexistente!
            '''
        
        context = {
            'resposta': mensagem
        }

        return render(request, "compra_ingressos/login.html", context)
        
    else:
        return render(request, "compra_ingressos/login.html")