from django.db import models


class Usuario(models.Model):

    nombre = models.CharField(max_length=100)

    apellido = models.CharField(max_length=100)

    correo = models.EmailField(unique=True)

    telefono = models.CharField(max_length=20)

    ciudad = models.CharField(max_length=100)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Formacion(models.Model):

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='formaciones'
    )

    titulo = models.CharField(max_length=150)

    institucion = models.CharField(max_length=150)

    estado = models.CharField(max_length=50)

    año = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"


class Experiencia(models.Model):

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='experiencias'
    )

    cargo = models.CharField(max_length=150)

    empresa = models.CharField(max_length=150)

    fecha_inicio = models.DateField()

    fecha_fin = models.DateField(
        null=True,
        blank=True
    )

    descripcion = models.TextField()

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"
    

class Habilidad(models.Model):

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='habilidades'
    )

    nombre = models.CharField(max_length=100)

    nivel = models.PositiveIntegerField(
        default=50
    )

    def __str__(self):
        return f"{self.nombre} - {self.nivel}%"
    
    
    