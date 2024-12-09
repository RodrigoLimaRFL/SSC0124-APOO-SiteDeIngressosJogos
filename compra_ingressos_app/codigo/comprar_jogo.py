from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

#importações dos modelos (classes) necessários para o UC Abrir Conta
#from compra_ingressos_app.models import usuario, jogo

# Post => envio dados para acesso BD
# Get => envio dados sem acesso ao BD
def comprarIngresso(request):
    if request.method == "POST":
        idJogo = request.POST['idJogo']

        jogo = ConsultarJogo(idJogo)

        if(jogo):
            return redirect('', idJogo = jogo.idJogo)
        else:
            return redirect("buscarJogo")

    else:
        return render(request, "compra_ingressos/compraIngresso.html")