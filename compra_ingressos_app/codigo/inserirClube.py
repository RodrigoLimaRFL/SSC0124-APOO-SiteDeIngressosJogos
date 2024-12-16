from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

from compra_ingressos_app.models import Clube

from compra_ingressos_app.decorators import gerente_required

@gerente_required
def novoClube(request):
    '''
        Cadastro de um novo clube no sistema. Apenas gerentes podem acessar essa página.
    '''
    if request.method == 'POST':
        # Obtém dados do formulário
        nomeClube = request.POST['nomeClube']
        divisao = request.POST['divisao']
        cidadeOrigem = request.POST['cidadeOrigem']

        if (Clube.doesClubeExist(nomeClube)):
            mensagem = "Erro! O clube já existe."
            context = {'resposta': mensagem}
            return render(request, "compra_ingressos/novoClube.html", context)

        mensagem = f'''
            Clube cadastrado com sucesso!
            Nome do clube: {nomeClube}
            Divisão do clube: {divisao}
            Cidade de origem: {cidadeOrigem}    
        '''

        context = {
            'resposta': mensagem
        }

        # Cria o clube
        clube = Clube(nomeClube = nomeClube, 
                      divisao = divisao, 
                      cidadeOrigem = cidadeOrigem)
        clube.registrarClube()

        return render(request, "compra_ingressos/novoClube.html", context)
    else:
        return render(request, "compra_ingressos/novoClube.html")