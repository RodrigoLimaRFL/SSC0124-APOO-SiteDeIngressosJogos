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
        nome = request.POST.get('nomePessoa', '').strip()
        cpf = request.POST.get('cpfPessoa', '').strip()
        dateNasc = request.POST.get('birthdate', '').strip()
        telefone = request.POST.get('telefonePessoa', '').strip()
        email = request.POST.get('emailPessoa', '').strip()
        senha = request.POST.get('senhaConta', '').strip()

        # Verificar campos vazios
        if not nome or not cpf or not dateNasc or not telefone or not email or not senha:
            mensagem = '''
                Todos os campos devem ser preenchidos!
            '''

            context = {
                'resposta': mensagem
            }

            return render(request, "compra_ingressos/criarConta.html", context)

        # Verifica se já existe um usuário com o cpf informado
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