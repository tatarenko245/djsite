from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Сторінка додатка Women")


def categories(request):
    return HttpResponse("<h1> Сторінка за категоріями</h1>")