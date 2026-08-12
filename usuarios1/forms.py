from django import forms

from .models import Usuario, Formacion


class UsuarioForm(forms.ModelForm):

    class Meta:

        model = Usuario

        fields = [
            'nombre',
            'apellido',
            'correo',
            'telefono',
            'ciudad',
        ]

        widgets = {

            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Yeison'
            }),

            'apellido': forms.TextInput(attrs={
                'placeholder': 'Ej: Estiben'
            }),

            'correo': forms.EmailInput(attrs={
                'placeholder': 'Ej: correo@email.com'
            }),

            'telefono': forms.TextInput(attrs={
                'placeholder': 'Ej: 3001234567'
            }),

            'ciudad': forms.TextInput(attrs={
                'placeholder': 'Ej: Popayán'
            }),
        }


class FormacionForm(forms.ModelForm):

    class Meta:

        model = Formacion

        fields = [
            'titulo',
            'institucion',
            'estado',
            'año',
        ]

        widgets = {

            'titulo': forms.TextInput(attrs={
                'placeholder': 'Ej: Tecnólogo en ADSO'
            }),

            'institucion': forms.TextInput(attrs={
                'placeholder': 'Ej: SENA'
            }),

            'estado': forms.TextInput(attrs={
                'placeholder': 'Ej: En curso'
            }),

            'año': forms.NumberInput(attrs={
                'placeholder': 'Ej: 2026'
            }),
        }