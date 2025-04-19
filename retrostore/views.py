from django.shortcuts import render

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
    return render(request, './productos/producto.html')

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

