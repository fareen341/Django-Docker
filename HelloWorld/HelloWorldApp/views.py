from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return HttpResponse("Hello world from django v3 ... from ansible script using CI/CD pipeline ...v2.0!!")
