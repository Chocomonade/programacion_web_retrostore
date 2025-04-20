from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.register, name='register'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/atari', views.categoria_atari, name='categoria_atari'),
    path('categorias/dreamcast', views.categoria_dreamcast, name='categoria_dreamcast'),
    path('categorias/nintendo', views.categoria_nintendo, name='categoria_nintendo'),
    path('categorias/playstation', views.categoria_playstation, name='categoria_playstation'),
    path('categorias/sega', views.categoria_sega, name='categoria_sega'),
    path('perfil/', views.perfil, name='perfil'),
    path('productos/', views.productos, name='productos'),
    path('productos/atari/atari_01', views.atari_01, name='atari_01'),
    path('productos/atari/atari_02', views.atari_02, name='atari_02'),
    path('productos/dreamcast/dreamcast_01', views.dreamcast_01, name='dreamcast_01'),
    path('productos/dreamcast/dreamcast_02', views.dreamcast_02, name='dreamcast_02'),
    path('productos/nintendo/nintendo_01', views.nintendo_01, name='nintendo_01'),
    path('productos/nintendo/nintendo_02', views.nintendo_02, name='nintendo_02'),
    path('productos/plastation/plastation_01', views.plastation_01, name='plastation_01'),
    path('productos/plastation/plastation_02', views.plastation_02, name='plastation_02'),
    path('productos/sega/sega_01', views.sega_01, name='sega_01'),
    path('productos/sega/sega_02', views.sega_02, name='sega_02'),
    path('perfil/nuevo_producto', views.nuevo_producto, name='nuevo_producto'),
    path('', views.index, name='index'),
    path('registro/', views.register, name='register'),
    
    # login/logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin-view/', views.solo_para_admins, name='admin_view'),
    path('perfil/editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar_password/', auth_views.PasswordChangeView.as_view(
        template_name='perfil/cambiar_password.html',
        success_url='/perfil/'
    ), name='cambiar_password'),
    path('perfil/nuevo_producto', views.nuevo_producto, name='nuevo_producto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)