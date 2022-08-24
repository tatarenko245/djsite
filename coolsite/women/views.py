from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse("Сторінка додатка Women")


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1> Сторінка за категоріями</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1> Архів за роками</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдено.</h1>")