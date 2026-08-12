from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.inicio,
        name='inicio_usuarios1'
    ),

    path(
        'registro/',
        views.registro,
        name='registro_usuario'
    ),

    path(
        'editar/',
        views.editar_perfil,
        name='editar_perfil'
    ),

    path(
        'formacion/',
        views.agregar_formacion,
        name='agregar_formacion'
    ),

]