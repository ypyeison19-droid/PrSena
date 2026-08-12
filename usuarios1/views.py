from django.shortcuts import render, redirect

from .forms import UsuarioForm, FormacionForm
from .models import Usuario, Formacion


def inicio(request):

    usuario = Usuario.objects.last()

    return render(
        request,
        'usuarios1/inicio.html',
        {'usuario': usuario}
    )


def registro(request):

    if request.method == 'POST':

        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            return redirect('inicio_usuarios1')

    else:

        formulario = UsuarioForm()

    return render(
        request,
        'usuarios1/registro.html',
        {'formulario': formulario}
    )


def editar_perfil(request):

    usuario = Usuario.objects.last()

    if request.method == 'POST':

        formulario = UsuarioForm(
            request.POST,
            instance=usuario
        )

        if formulario.is_valid():

            formulario.save()

            return redirect('inicio_usuarios1')

    else:

        formulario = UsuarioForm(
            instance=usuario
        )

    return render(
        request,
        'usuarios1/editar.html',
        {'formulario': formulario}
    )


def agregar_formacion(request):

    usuario = Usuario.objects.last()

    if request.method == 'POST':

        formulario = FormacionForm(request.POST)

        if formulario.is_valid():

            formacion = formulario.save(commit=False)

            formacion.usuario = usuario

            formacion.save()

            return redirect('inicio_usuarios1')

    else:

        formulario = FormacionForm()

    return render(
        request,
        'usuarios1/formacion.html',
        {'formulario': formulario}
    )