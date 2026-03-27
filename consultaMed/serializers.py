from rest_framework import serializers
from .models import Medico, Paciente, Consulta

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


