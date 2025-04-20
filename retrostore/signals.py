from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PerfilUsuario
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)
