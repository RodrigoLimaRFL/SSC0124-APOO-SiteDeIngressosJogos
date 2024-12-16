from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from compra_ingressos_app.models import Jogo, Usuario, RegistroCompra

from compra_ingressos_app.decorators import usuario_normal_required


@usuario_normal_required
def comprarIngresso(request):
    '''
        Realiza a compra de um jogo. O usuário deve estar logado para realizar a compra.
    '''
    # Recupera todos os jogos disponíveis para compra
    jogos = Jogo.objects.all()

    # Se GET, então exibe os jogos
    if request.method == "GET":
        context = {
            "jogos": jogos
        }

        return render(request, "compra_ingressos/compraIngresso.html", context)
    
    # Se POST, então realiza a compra com id fornecido pelo usuário
    else:
        # Obtém o id do jogo
        idJogo = request.POST['id']
        jogo = Jogo.recuperarID(idJogo)

        if not jogo: # Caso o id fornecido seja inválido
            mensagem = '''
                Jogo não encontrado. Tente novamente!
            '''

            context = {
                'resposta': mensagem,
                'jogos': jogos
            }

            return render(request, "compra_ingressos/compraIngresso.html", context)

        momentoAtual = datetime.now()

        # Cria um registro de compra
        registro = RegistroCompra(dataRegistro = momentoAtual.date(), horaRegistro = momentoAtual.time(), jogoCompra = jogo, precoCompra = 50)
        registro.salvarRegistro()

        mensagem = '''
            Jogo comprado com sucesso!
        '''

        context = {
            'resposta': mensagem,
            'jogos': jogos
        }

        return render(request, "compra_ingressos/compraIngresso.html", context)