from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Medico(models.Model):
    nombres      = models.CharField(max_length=50)
    ap_paterno   = models.CharField(max_length=50)
    ap_materno   = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    licencia     = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Dr. {self.nombres} {self.ap_paterno} {self.ap_materno} - {self.especialidad} {self.licencia}"


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
        choices = PacienteSexo,
        default = PacienteSexo.MASCULINO
    )
    direccion  = models.CharField(max_length=100)
    matricula_clinica = models.CharField(max_length=50)
    peso_al_nacer     = models.DecimalField(decimal_places=2, max_digits=10)
    alimentacion      = models.CharField(
        max_length=5,
        choices=PacienteAlimentacion.choices,
        default=PacienteAlimentacion.NATURAL
    )

    def __str__(self):
        return f"Pte. {self.nombres} {self.ap_paterno} {self.ap_materno} - {self.matricula_clinica}"
            
    # Validación personalizada 1: Edad mínima
    fecha_nacimiento = models.DateField()

    def clean(self):
        # Ejemplo: Validar que no se registren pacientes con fechas futuras
        import datetime
        if self.fecha_nacimiento > datetime.date.today():
            raise ValidationError("La fecha de nacimiento no puede ser futura.")

class Consulta(models.Model):
    paciente    = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico      = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha       = models.DateTimeField(auto_now_add=True)
    edad        = models.IntegerField()
    talla       = models.DecimalField(decimal_places=2, max_digits=5)
    peso        = models.DecimalField(decimal_places=2, max_digits=5)
    temperatura = models.DecimalField(decimal_places=2, max_digits=5)
    # fc = models.DecimalField(decimal_places=2, max_digits=5)
    # pa = models.DecimalField(decimal_places=2, max_digits=5)
    # fr = models.DecimalField(decimal_places=2, max_digits=5)
    subjetivo      = models.TextField()
    objetivo       = models.TextField()
    analisis       = models.TextField()
    plan_de_accion = models.TextField()
    cie            = models.TextField()
    mps            = models.TextField()
    
    # Validación personalizada 2: Contenido mínimo
    def clean(self):
        if len(self.subjetivo) < 10:
            raise ValidationError("La descripción de los síntomas es demasiado corta.")

class Receta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    medicamento = models.TextField()
    indicacion  = models.TextField()