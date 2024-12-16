from django.urls import path
#importa as funções de controle (controllers em MVC) que em django estão no views.py
from compra_ingressos_app import views

#A seguir são configuradas as rotas da nossa aplicação
urlpatterns = [
    path("", views.home, name="home"),

    path("novoJogo/", views.novoJogo, name="novoJogo"),
    path("realizarLogin/", views.realizarLogin, name="realizarLogin"),
    path("compraIngresso/", views.comprarIngresso, name="compraIngresso"),
    path("novoClube/", views.novoClube, name="novoClube"),
    path("criarConta/", views.criarConta, name="criarConta"),
    path('logout/', views.logout_view, name='logout'),
    path('aviso_login/', views.aviso_login, name='aviso_login'),
    path('acesso_negado/', views.acesso_negado, name='acesso_negado'),
   
]

