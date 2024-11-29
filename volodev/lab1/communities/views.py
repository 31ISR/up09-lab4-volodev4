from django.shortcuts import render
from django.http import HttpResponse

def communities_view(request):
    return HttpResponse("<h1>Список сообществ</h1>")
