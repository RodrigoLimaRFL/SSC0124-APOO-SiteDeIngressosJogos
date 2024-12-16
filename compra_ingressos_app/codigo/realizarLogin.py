from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from compra_ingressos_app.models import Usuario

def realizarLogin(request):
    '''
        Realiza o login do usuário no sistema. Salva o cpf, o nome e o tipo do usuário na sessão.
    '''
    if request.session.get('usuario_id'): # Já está logado
        return render(request, "compra_ingressos/login.html", {
            "usuario_nome": request.session.get('usuario_nome'),
            "logado": True
        })

    if request.method == "POST":
        # Obtém dados do formulário
        cpf = request.POST.get('cpfPessoa')
        senhaDigitada = request.POST.get('senhaConta')

        usuario = Usuario.consultarCPF(cpf)

        if usuario:
            if check_password(senhaDigitada, usuario.senha): # Senha correta
                # Salva dados na sessão
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nome'] = usuario.nome
                request.session['usuario_tipo'] = usuario.tipoUsuario

                return redirect('home')
            else: # Errou a senha
                mensagem = "Senha incorreta. Tente novamente!"
        else: # Usuário não existe
            mensagem = "Usuário inexistente!"

        return render(request, "compra_ingressos/login.html", {"resposta": mensagem})

    return render(request, "compra_ingressos/login.html", {"logado": False})
