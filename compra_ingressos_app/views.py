from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

# Métodos view importados. São grandes, por isso foram criados em arquivos separados.
from compra_ingressos_app.codigo.inserirJogo import novoJogo
from compra_ingressos_app.codigo.realizarLogin import realizarLogin
from compra_ingressos_app.codigo.comprar_jogo import comprarIngresso
from compra_ingressos_app.codigo.inserirClube import novoClube
from compra_ingressos_app.codigo.criarConta import criarConta


#a seguir são definidas as funções que possuem lógica dos controladores no padrão MVC

# função default da interface inicial do sistema 'home'
def home(request):
    #método executado quando o usuário está na interface inicial do sistema. 
    #Envia-se uma solicitação de renderização da interface home.html
    return render(request, "compra_ingressos/home.html")


# Pagina de logout
def logout_view(request):
    request.session.flush()  # Remove todos os dados da sessão
    return redirect('realizarLogin')  # Redireciona para a página de login


# Página de aviso que não está logado
def aviso_login(request):
    return render(request, "compra_ingressos/aviso_login.html")


# Página de aviso que não tem as credenciais necessárias
def acesso_negado(request):
    return render(request, "compra_ingressos/acesso_negado.html")