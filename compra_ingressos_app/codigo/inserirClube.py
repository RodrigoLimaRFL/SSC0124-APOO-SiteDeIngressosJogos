from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

from compra_ingressos_app.models import Clube

def novoClube(request):
    if request.method == 'POST':
        nomeClube = request.POST['nomeClube']
        divisao = request.POST['divisao']
        cidadeOrigem = request.POST['cidadeOrigem']

        mensagem = f'''
            Clube cadastrado com sucesso!
            Nome do clube: {nomeClube}
            Divisão do clube: {divisao}
            Cidade de origem: {cidadeOrigem}    
        '''

        context = {
            'resposta': mensagem
        }

        clube = Clube(nomeClube = nomeClube, divisao = divisao, cidadeOrigem = cidadeOrigem)
        clube.registrarClube()

        return render(request, "compra_ingressos/novoClube.html", context)
    else:
        return render(request, "compra_ingressos/novoClube.html")