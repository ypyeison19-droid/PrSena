from django.shortcuts import render, redirect

from .models import Usuario, Formacion, Experiencia, Habilidad

from .forms import UsuarioForm, FormacionForm, ExperienciaForm, HabilidadForm


def inicio(request):

    usuario = Usuario.objects.last()

    formaciones = Formacion.objects.filter(
        usuario=usuario
    )

    experiencias = Experiencia.objects.filter(
        usuario=usuario
    )

    habilidades = Habilidad.objects.filter(
        usuario=usuario
    )

    return render(
        request,
        'usuarios1/inicio.html',
        {
            'usuario': usuario,
            'formaciones': formaciones,
            'experiencias': experiencias,
            'habilidades': habilidades
        }
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
    
def agregar_experiencia(request):

    usuario = Usuario.objects.last()

    if request.method == 'POST':

        formulario = ExperienciaForm(request.POST)

        if formulario.is_valid():

            experiencia = formulario.save(commit=False)

            experiencia.usuario = usuario

            experiencia.save()

            return redirect('inicio_usuarios1')

    else:

        formulario = ExperienciaForm()

    return render(
        request,
        'usuarios1/experiencia.html',
        {
            'formulario': formulario
        }
    )
    
def agregar_habilidad(request):

    usuario = Usuario.objects.last()

    if request.method == 'POST':

        formulario = HabilidadForm(request.POST)

        if formulario.is_valid():

            habilidad = formulario.save(commit=False)

            habilidad.usuario = usuario

            habilidad.save()

            return redirect('inicio_usuarios1')

    else:

        formulario = HabilidadForm()

    return render(
        request,
        'usuarios1/habilidad.html',
        {
            'formulario': formulario
        }
    )
    
    
def editar_habilidad(request, id):

    habilidad = Habilidad.objects.get(id=id)

    if request.method == 'POST':

        formulario = HabilidadForm(
            request.POST,
            instance=habilidad
        )

        if formulario.is_valid():

            formulario.save()

            return redirect('inicio_usuarios1')

    else:

        formulario = HabilidadForm(
            instance=habilidad
        )

    return render(
        request,
        'usuarios1/habilidad.html',
        {
            'formulario': formulario,
            'editar': True
        }
    )


def eliminar_habilidad(request, id):

    habilidad = Habilidad.objects.get(id=id)

    if request.method == 'POST':

        habilidad.delete()

        return redirect('inicio_usuarios1')

    return render(
        request,
        'usuarios1/eliminar_habilidad.html',
        {
            'habilidad': habilidad
        }
    )