from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Medico, Paciente, Consulta
from .serializers import MedicoSerializer, PacienteSerializer, ConsultaSerializer

# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo")

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

