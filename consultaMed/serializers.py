from rest_framework import serializers
from .models import Medico, Paciente, Consulta, Receta

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = "__all__"

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = "__all__"


class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = "__all__"
