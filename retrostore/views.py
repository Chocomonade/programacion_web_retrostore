from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from .forms import EditarPerfilForm
from retrostore.models import Producto, Categoria

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'registro.html')

def categorias(request):
    return render(request, './categorias/todas.html')

def categoria_atari(request):
    return render(request, './categorias/atari.html')

def categoria_dreamcast(request):
    return render(request, './categorias/dreamcast.html')

def categoria_nintendo (request):
    return render(request, './categorias/nintendo.html')

def categoria_playstation (request):
    return render(request, './categorias/playstation.html')

def categoria_sega (request):
    return render(request, './categorias/sega.html')

def perfil(request):
    return render(request, './perfil/perfil.html')

def productos(request):
    return render(request, './productos/todos.html')

def atari_01(request):
    return render(request, './productos/atari/atari_01.html')

def atari_02(request):
    return render(request, './productos/atari/atari_02.html')

def dreamcast_01(request):
    return render(request, './productos/dreamcast/dreamcast_01.html')

def dreamcast_02(request):
    return render(request, './productos/dreamcast/dreamcast_02.html')

def nintendo_01(request):
    return render(request, './productos/nintendo/nintendo_01.html')

def nintendo_02(request):
    return render(request, './productos/nintendo/nintendo_02.html')

def plastation_01(request):
    return render(request, './productos/plastation/plastation_01.html')

def plastation_02(request):
    return render(request, './productos/plastation/plastation_02.html')

def sega_01(request):
    return render(request, './productos/sega/sega_01.html')

def sega_02(request):
    return render(request, './productos/sega/sega_02.html')

def nuevo_producto(request):
    return render(request, './perfil/nuevo_producto.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página principal después del login
    else:
        form = AuthenticationForm()
    
    # Personaliza los campos del formulario
    form.fields['username'].widget.attrs.update({
        'class': 'form-control bg-light',
        'placeholder': 'Username'
    })
    form.fields['password'].widget.attrs.update({
        'class': 'form-control bg-light',
        'placeholder': 'Password'
    })
    
    return render(request, 'login.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'perfil/perfil.html')

@login_required
def solo_para_admins(request):
    if request.user.perfilusuario.rol != 'admin':
        return redirect('index')  # o mostrar error

    return render(request, 'admin_view.html')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar clases a todos los campos
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[fieldname].label or fieldname
            })

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registro.html', {'form': form})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=request.user)

    return render(request, 'perfil/editar_perfil.html', {'form': form})

from django.shortcuts import render, redirect
from retrostore.models import Producto, Categoria

def nuevo_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        imagen = request.FILES.get('imagen')
        categoria_id = request.POST.get('categoria')

        # Validamos si existe la categoría seleccionada
        try:
            categoria = Categoria.objects.get(id=categoria_id)
        except Categoria.DoesNotExist:
            return render(request, 'perfil/nuevo_producto.html', {
                'categorias': Categoria.objects.all(),
                'error': 'Categoría inválida seleccionada.'
            })

        # Crear y guardar producto
        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            imagen=imagen,
            categoria=categoria
        )
        producto.save()

        return redirect('perfil')  # Redirige tras éxito

    # GET normal
    categorias = Categoria.objects.all()
    return render(request, 'perfil/nuevo_producto.html', {'categorias': categorias})

