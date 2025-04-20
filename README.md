
# RetroPlay 🎮

Proyecto de Programación Web que permite el registro de usuarios, productos y visualización de un carrito de compras. Desarrollado en Django, con base de datos Oracle.

---

## 🚀 Requisitos

- Python 3.12+
- Oracle Database Express Edition (XE)
- Oracle Instant Client (con cx_Oracle)
- Django 5.2+
- VS Code u otro IDE
- SQL Developer (opcional)

---

## 🔧 Instalación

### 1. Clona este repositorio

```bash
git clone https://github.com/tuusuario/retroplay.git
cd retroplay
```

### 2. Crea y activa entorno virtual

```bash
python -m venv env
env\Scripts\activate  # en Windows
```

### 3. Instala dependencias

```bash
pip install -r requirements.txt
```

---

## 🧠 Configuración de Oracle XE

### 1. Asegúrate de tener:
- Oracle XE instalado y corriendo
- Usuario creado (por ejemplo: `system` con contraseña `Oracle1234`)
- Puerto por defecto (`1521`) y nombre de servicio `XE`

### 2. Configura `settings.py` en Django:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'XE',
        'USER': 'system',
        'PASSWORD': 'Oracle1234',
        'HOST': 'localhost',
        'PORT': '1521',
    }
}
```

---

## 📂 Migraciones y carga de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

> Puedes ejecutar el script `oracle_datos_iniciales.sql` para crear categorías predefinidas u otros datos básicos.

---

## ⚙️ Ejecución del proyecto

```bash
python manage.py runserver
```

Abre tu navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Acceso al administrador

```bash
python manage.py createsuperuser
```

---

## 📝 Funcionalidades incluidas

- Registro y login de usuarios
- Validaciones de contraseña seguras
- Edición de perfil y cambio de contraseña
- Registro de productos
- Categorización dinámica desde Oracle
- Carrito de compras visual
- Protección de rutas
- Panel admin para gestión interna

---

