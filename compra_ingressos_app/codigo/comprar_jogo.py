from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from compra_ingressos_app.models import Jogo, Usuario

# Recupera a lista de todos os jogos e mostra na página
def comprarIngresso(request):
    if request.method == "GET":
        jogos = Jogo.recuperarJogo(clube = "Vasco")
        #jogos = Jogo.objects.all()

        return render(request, "compra_ingressos/compraIngresso.html", jogos)

'''def confirmarCompra(request, Jogo, Preco):
    data_compra = datetime.now().date()
    horario_compra = datetime.now().strftime('%H:%M:%S')

    compra = RegistroCompra(
        dataCompra = data_compra,
        horarioCompra = horario_compra,
        jogo = Jogo,
        precoFinal = Preco
    )

    compra.savarDados()

    return render(request, "compra_ingressos/confirmaCompra.html", compra)'''