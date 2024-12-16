from django.shortcuts import redirect
from functools import wraps

def login_required_custom(view_func):
    """Verifica se o usuário está logado."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            return redirect('aviso_login')  # Redireciona para a página de aviso
        return view_func(request, *args, **kwargs)
    return wrapper

def gerente_required(view_func):
    """Verifica se o usuário é gerente (tipoUsuario=1)."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        usuario_id = request.session.get('usuario_id')
        tipo_usuario = request.session.get('usuario_tipo')

        if not usuario_id:  # Verifica se o usuário está logado
            return redirect('aviso_login')
        if tipo_usuario != 1:  # Verifica se é gerente
            return redirect('acesso_negado')  # Redireciona para uma página de acesso negado
        return view_func(request, *args, **kwargs)
    return wrapper

def usuario_normal_required(view_func):
    """Verifica se o usuário é normal (tipoUsuario=0)."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        usuario_id = request.session.get('usuario_id')
        tipo_usuario = request.session.get('usuario_tipo')

        if not usuario_id:  # Verifica se o usuário está logado
            return redirect('aviso_login')
        if tipo_usuario != 0:  # Verifica se é usuário normal
            return redirect('acesso_negado')  # Redireciona para uma página de acesso negado
        return view_func(request, *args, **kwargs)
    return wrapper
