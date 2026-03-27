import datetime
from django.core.exceptions import ValidationError

def validar_fecha_nacimiento(value):
    """Valida que la fecha de nacimiento no sea futura."""
    if value > datetime.date.today():
        raise ValidationError("La fecha de nacimiento no puede ser futura.")

def validar_longitud_subjetivo(value):
    """Valida que el texto tenga al menos 10 caracteres."""
    if len(value) < 10:
        raise ValidationError("La descripción de los síntomas es demasiado corta.")