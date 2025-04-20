from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re 

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        if len(pwd) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", pwd):
            raise ValidationError("Debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", pwd):
            raise ValidationError("Debe contener al menos una letra minúscula.")
        if not re.search(r"\d", pwd):
            raise ValidationError("Debe contener al menos un número.")
        if not re.search(r"[^\w\s]", pwd):
            raise ValidationError("Debe contener al menos un carácter especial.")
        return pwd

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        pwd2 = cleaned_data.get('password2')

        if pwd and pwd2 and pwd != pwd2:
            raise ValidationError("Las contraseñas no coinciden.")

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
