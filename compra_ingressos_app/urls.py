from django.urls import path
#importa as funções de controle (controllers em MVC) que em django estão no views.py
from compra_ingressos_app import views

#No Django, a configuração de URLs é feita por meio de um sistema de roteamento que mapeia URLs (endereços web) para views (funções ou controladores que processam as requisições). 
#O arquivo de configuração de URLs em Django é geralmente o urls.py, onde você define as rotas para a aplicação.
#A configuração de path nas URLs é feita utilizando a função path() (ou re_path() em casos mais avançados). 
#A função path() permite que você defina uma URL específica e associe ela a uma view, e, além disso, 
#você pode passar parâmetros dinâmicos para a view através da URL.

#A seguir são configuradas as rotas da nossa aplicação
urlpatterns = [
    #a URL vazia "", será associada à função (controlador) 'home' no views.py. A chamada a essa função é views.home.
    #O name='home' serve para dar um nome à URL, o que facilita sua referência em templates e em redirecionamentos.
    path("", views.home, name="home"),

    path("novoJogo/", views.novoJogo, name="novoJogo"),
    path("realizarLogin/", views.realizarLogin, name="realizarLogin"),
    path("compraIngresso/", views.comprarIngresso, name="compraIngresso"),
    path("novoClube/", views.novoClube, name="novoClube"),
    path("criarConta/", views.criarConta, name="criarConta"),
    path('logout/', views.logout_view, name='logout'),
    path('aviso_login/', views.aviso_login, name='aviso_login'),
    path('acesso_negado/', views.acesso_negado, name='acesso_negado'),
   
    #a URL "consultarCliente/", será associada à função (controlador) consultarCliente no views.py. 
    # A chamada a essa função é views.consultarCliente
    #o nome para referenciar a rota durante o redirecionamento é "consultarCliente"
    #path("consultarCliente/", views.consultarCliente, name="consultarCliente"),

    #similarmente acontece com as seguintes configurações de redirecionamentos    
    #path("atualizarDadosCliente/", views.atualizarDadosCliente, name="atualizarDadosCliente"),
    #path("abrirConta/", views.abrirConta, name="abrirConta"),
    #path("emitirExtrato/", views.emitirExtrato, name="emitirExtrato"),
    #path("emitirSaldo/", views.emitirSaldo, name="emitirSaldo"),
    #path("encerrarConta/", views.encerrarConta, name="encerrarConta"),
    #path("realizarDeposito/", views.realizarDeposito, name="realizarDeposito"),
    #path("realizarSaque/", views.realizarSaque, name="realizarSaque"),
    #path("gerenciarClientes/", views.gerenciarClientes, name="gerenciarClientes"),
    #A seguinte configuração de redirecionamento é um pouco diferente, pois adiciona parâmetros dinâmicos na URL
    # você pode capturar valores passados na URL e passá-los para as views como argumentos.
    #Por exemplo, o parâmetro cpfPessoa está sendo enviado como argumento para a função (controlador) atualizarDadosCliente que está em views.py
    #sendo assim, a função atualizarDadosClientes poderá pegar cpfPessoa como variável local na sua execução.
    #path("atualizarDadosCliente/<cpfPessoa>/", views.atualizarDadosCliente, name="atualizarDadosCliente"),
]

