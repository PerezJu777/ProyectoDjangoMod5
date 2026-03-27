from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Medico, Paciente, Consulta, Receta
from .serializers import MedicoSerializer, PacienteSerializer, ConsultaSerializer, RecetaSerializer

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


@api_view(["GET"])
def recetas_view(request):
    try:
        queryset = list(Receta.objects.all().values())
        return JsonResponse(
            {
                "recetas": queryset
            },
        safe = False,
        status = 200,
    )
    except Exception as e:
        return JsonResponse({"message ": str(e)}, status = 400)