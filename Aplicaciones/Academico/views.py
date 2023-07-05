#from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.


def home(request):
    cursosListados = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursosListados})



#return HttpResponse("<h1>Hola mundo!</h1>"