from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

#importações dos modelos (classes) necessários para o UC Abrir Conta
#from compra_ingressos_app.models import usuario, jogo

# Recupera a lista de todos os jogos e 
def comprarIngresso(request):
    if request.method == "GET":
        jogos = Jogo.objects.all()

        return render(request, "compra_ingresso/compraIngresso.html", {'jogos':jogos})
            