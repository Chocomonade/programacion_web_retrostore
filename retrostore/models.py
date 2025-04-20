from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    ROLES = [
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=10, choices=ROLES, default='cliente')

    def __str__(self):
        return f"{self.user.username} - {self.get_rol_display()}"

from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # ⬅️ AÑADE ESTO
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

class DireccionDespacho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    tipo_direccion = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.calle} #{self.numero}"

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="Pendiente")

    def __str__(self):
        return f"Orden #{self.id} de {self.cliente}"

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto} x{self.cantidad}"



