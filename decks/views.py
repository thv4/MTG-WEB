from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("HOLA ESTO ES LA PÁGINA INICAL")
