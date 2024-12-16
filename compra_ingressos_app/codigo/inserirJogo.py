from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from compra_ingressos_app.models import Jogo
from compra_ingressos_app.models import Clube

from compra_ingressos_app.decorators import gerente_required


@gerente_required
def novoJogo(request):
    '''
        Cadastra um novo jogo no sistema. Apenas gerentes podem acessar essa página.
    '''
    if request.method == 'POST':
        # Obtém dados do formulário
        nomeClubeCasa = request.POST['clubeCasa']
        nomeClubeFora = request.POST['clubeFora']
        data = request.POST['data']
        hora = request.POST['hora']
        preco = request.POST['preco']
        estadio = request.POST['estadio']
        numero_cadeiras = request.POST['numero_cadeiras']

        try:
            clubeCasa = Clube.objects.get(nomeClube=nomeClubeCasa) # busca o clube pelo nome no BD
            clubeFora = Clube.objects.get(nomeClube=nomeClubeFora)

            if clubeCasa == clubeFora:
                mensagem = "O clube da casa não pode ser o mesmo que o clube de fora."
                context = {'resposta': mensagem}
                return render(request, "compra_ingressos/novoJogo.html", context)
            
            data = datetime.strptime(data, '%Y-%m-%d').date()  # 'YYYY-MM-DD' formato
            hora = datetime.strptime(hora, '%H:%M').time()    # 'HH:MM' formato
            preco = float(preco)  # Converte pra float
            numero_cadeiras = int(numero_cadeiras)  # Converte pra int

            # Cria o jogo
            jogo = Jogo(
                clubeCasa=clubeCasa,
                clubeFora=clubeFora,
                data=data,
                hora=hora,
                preco=preco,
                estadio=estadio,
                numero_cadeiras=numero_cadeiras
            )
            jogo.registrarJogo()

            mensagem = f'''
                Jogo cadastrado com sucesso!
                Clube Casa: {clubeCasa.nomeClube}
                Clube Fora: {clubeFora.nomeClube}
                Data: {data}    
                Hora: {hora}
                Preço: {preco}
                Estádio: {estadio}
                Número de cadeiras: {numero_cadeiras}
            '''
            context = {'resposta': mensagem}
            return render(request, "compra_ingressos/novoJogo.html", context)
        
        except ObjectDoesNotExist:
            # If a club name doesn't match any entry
            mensagem = "Um dos clubes não existe. Verifique o nome dos clubes."
            context = {'resposta': mensagem}
            return render(request, "compra_ingressos/novoJogo.html", context)

        except ValueError as e:
            # Handle invalid data (e.g., incorrect date or number format)
            mensagem = f"Erro ao cadastrar jogo: {e}. Por favor, verifique os dados inseridos."
            context = {'resposta': mensagem}
            return render(request, "compra_ingressos/novoJogo.html", context)
        
    else:
        return render(request, "compra_ingressos/novoJogo.html")

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
        
        mensagem = f'''
            #Jogo cadastrado com sucesso!
            #Clube Casa: {nomeClubeCasa}
            #Clube Fora: {nomeClubeFora}
            #Data: {data}    
            #Hora: {hora}
            #Preço: {preco}
            #Estádio: {estadio}
            #Número de cadeiras: {numero_cadeiras}
        '''

        context = {
            'resposta': mensagem
        }

        jogo = Jogo(clubeCasa = clubeCasa, clubeFora = clubeFora, data = data, hora = hora, preco = preco, estadio = estadio, numero_cadeiras = numero_cadeiras)
        jogo.registrarJogo()

        return render(request, "compra_ingressos/novoJogo.html", context)
    else:
        return render(request, "compra_ingressos/novoJogo.html")
        '''