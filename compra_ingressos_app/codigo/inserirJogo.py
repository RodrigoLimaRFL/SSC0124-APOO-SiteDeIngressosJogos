from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

from compra_ingressos_app.models import Jogo


#from compra_ingressos_app.models import Jogo

def novoJogo(request):
    if request.method == 'POST':
        clubeCasa = request.POST['clubeCasa']
        clubeFora = request.POST['clubeFora']
        data = request.POST['data']
        hora = request.POST['hora']
        preco = request.POST['preco']
        estadio = request.POST['estadio']
        numero_cadeiras = request.POST['numero_cadeiras']

        '''
        # Consulta a existencia do jogo (n implementado)
        jogo = Jogo.consultarJogo(clubeCasa, clubeFora, data, hora, estadio)
        if jogo:
            mensagem = f"Jogo já cadastrado!"
            context = {
                'resposta': mensagem
            }
            return render(request, "compra_ingressos/novoJogo.html", context)
        
        # Cria o jogo (n implementado)
        jogo = Jogo(clubeCasa=clubeCasa, clubeFora=clubeFora, data=data, 
                    hora = hora, preco=preco, estadio=estadio, numero_cadeiras=numero_cadeiras)
        jogo.atualizarJogo()
        '''
        mensagem = f'''
            Jogo cadastrado com sucesso!
            Clube Casa: {clubeCasa}
            Clube Fora: {clubeFora}
            Data: {data}    
            Hora: {hora}
            Preço: {preco}
            Estádio: {estadio}
            Número de cadeiras: {numero_cadeiras}
        '''

        context = {
            'resposta': mensagem
        }

        jogo = Jogo(clubeCasa = clubeCasa, clubeFora = clubeFora, data = data, hora = hora, preco = preco, estadio = estadio, numero_cadeiras = numero_cadeiras)
        jogo.registrarJogo()

        return render(request, "compra_ingressos/novoJogo.html", context)
    else:
        return render(request, "compra_ingressos/novoJogo.html")