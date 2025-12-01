from django.http import HttpResponse
from django.shortcuts import render

def index(request): #HttpRequest
    return HttpResponse("<h1>First page of the application</h1>")
