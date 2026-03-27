from django.db import models
# Importamos los validadores que creamos
from .validators import validar_fecha_nacimiento, validar_longitud_subjetivo

class Medico(models.Model):
    nombres      = models.CharField(max_length=50)
    ap_paterno   = models.CharField(max_length=50)
    ap_materno   = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    licencia     = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Dr. {self.nombres} {self.ap_paterno} {self.ap_materno} - {self.especialidad}"


class PacienteAlimentacion(models.TextChoices):
    NATURAL    = 'Nat.', 'Natural'
    ARTIFICIAL = 'Arti.', 'Artificial'
    MIXTA      = 'Mixta', 'Mixta'

class PacienteSexo(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMENINO  = 'F', 'Femenino'

class Paciente(models.Model):
    nombres    = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    sexo       = models.CharField(
        max_length=1,
        choices=PacienteSexo.choices,
        default=PacienteSexo.MASCULINO
    )
    direccion         = models.CharField(max_length=100)
    matricula_clinica = models.CharField(max_length=50)
    peso_al_nacer     = models.DecimalField(decimal_places=2, max_digits=10)
    alimentacion      = models.CharField(
        max_length=5,
        choices=PacienteAlimentacion.choices,
        default=PacienteAlimentacion.NATURAL
    )
    # Aplicamos el validador directamente al campo
    fecha_nacimiento  = models.DateField(validators=[validar_fecha_nacimiento])

    def __str__(self):
        return f"Pte. {self.nombres} {self.ap_paterno} - {self.matricula_clinica}"


class Consulta(models.Model):
    paciente       = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico         = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha          = models.DateTimeField(auto_now_add=True)
    edad           = models.IntegerField()
    talla          = models.DecimalField(decimal_places=2, max_digits=5)
    peso           = models.DecimalField(decimal_places=2, max_digits=5)
    temperatura    = models.DecimalField(decimal_places=2, max_digits=5)
    
    # Aplicamos el validador aquí
    subjetivo      = models.TextField(validators=[validar_longitud_subjetivo])
    objetivo       = models.TextField()
    analisis       = models.TextField()
    plan_de_accion = models.TextField()
    cie            = models.TextField()
    mps            = models.TextField()

class Receta(models.Model):
    consulta    = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    medicamento = models.TextField()
    indicacion  = models.TextField()