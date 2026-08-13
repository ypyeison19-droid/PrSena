from django import forms

from .models import Usuario, Formacion, Experiencia


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


class ExperienciaForm(forms.ModelForm):

    class Meta:

        model = Experiencia

        fields = [
            'cargo',
            'empresa',
            'fecha_inicio',
            'fecha_fin',
            'descripcion',
        ]

        widgets = {

            'cargo': forms.TextInput(attrs={
                'placeholder': 'Ej: Auxiliar administrativo'
            }),

            'empresa': forms.TextInput(attrs={
                'placeholder': 'Ej: Empresa XYZ'
            }),

            'fecha_inicio': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'fecha_fin': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Describe tus principales funciones y responsabilidades',
                'rows': 5
            }),
        }