from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

from compra_ingressos_app.models import Usuario

def criarConta(request):
    if request.method == 'POST':
        nome = request.POST['nomePessoa']
        cpf = request.POST['cpfPessoa']
        dateNasc = request.POST['birthdate']
        telefone = request.POST['telefonePessoa']
        email = request.POST['emailPessoa']
        senha = request.POST['senhaConta']

        if Usuario.consultarCPF(cpf):
            mensagem = '''
                Já existe um usuário com este CPF.
            '''

            context = {
                'resposta': mensagem
            }

            return render(request, "compra_ingressos/criarConta.html", context)

        mensagem = f'''
            Usuário cadastrado com sucesso!
            Nome: {nome}
            Cpf = {cpf}
            Data de nascimento = {dateNasc}
            Telefone = {telefone}
            Email = {email}
        '''

        context = {
            'resposta': mensagem
        }

        user = Usuario(nome = nome, cpf = cpf, dateNasc = dateNasc, telefone = telefone, email = email, senha = senha)
        user.registrarUser()

        return render(request, "compra_ingressos/criarConta.html", context)
    else:
        return render(request, "compra_ingressos/criarConta.html")