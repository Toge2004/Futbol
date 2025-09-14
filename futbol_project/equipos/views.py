from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import EquipoFutbol
from .forms import RegistroUsuarioForm, EquipoFutbolForm

def home(request):
    equipos = EquipoFutbol.objects.filter(activo=True)[:3]
    return render(request, 'home.html', {'equipos': equipos})

def registro_usuario(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido/a.')
            return redirect('home')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido/a {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoFutbolForm(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.creado_por = request.user
            equipo.save()
            messages.success(request, '¡Equipo creado exitosamente!')
            return redirect('lista_equipos')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = EquipoFutbolForm()
    return render(request, 'equipo_form.html', {'form': form, 'titulo': 'Crear Equipo'})

@login_required(login_url='login')
def lista_equipos(request):
    equipos = EquipoFutbol.objects.all()
    return render(request, 'lista_equipos.html', {'equipos': equipos})

@login_required(login_url='login')
def editar_equipo(request, pk):
    equipo = get_object_or_404(EquipoFutbol, pk=pk)
    if request.method == 'POST':
        form = EquipoFutbolForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Equipo actualizado exitosamente!')
            return redirect('lista_equipos')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = EquipoFutbolForm(instance=equipo)
    return render(request, 'equipo_form.html', {'form': form, 'titulo': 'Editar Equipo'})

@login_required(login_url='login')
def eliminar_equipo(request, pk):
    equipo = get_object_or_404(EquipoFutbol, pk=pk)
    if request.method == 'POST':
        equipo.delete()
        messages.success(request, '¡Equipo eliminado exitosamente!')
        return redirect('lista_equipos')
    return render(request, 'confirmar_eliminar.html', {'equipo': equipo})