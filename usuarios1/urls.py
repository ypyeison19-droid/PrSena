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

    path(
        'experiencia/',
        views.agregar_experiencia,
        name='agregar_experiencia'
    ),

    path(
        'habilidad/',
        views.agregar_habilidad,
        name='agregar_habilidad'
    ),

    path(
        'habilidad/<int:id>/editar/',
        views.editar_habilidad,
        name='editar_habilidad'
    ),

    path(
        'habilidad/<int:id>/eliminar/',
        views.eliminar_habilidad,
        name='eliminar_habilidad'
    ),

]