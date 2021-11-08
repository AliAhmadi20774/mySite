from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

def index_view(request):
    return HttpResponse("<h1>HoME PagE!</h1>")

def about_view(request):
    return HttpResponse("<h1>AboUt !</h1>")

def contact_view(request):
    return HttpResponse("<h1>ConTact</h1>")



