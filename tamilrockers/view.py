from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .soup1tamilmv.index import movieList
import json


def sample():
    with open('/home/varun/Desktop/tamilrockers/tamilrockers/soup1tamilmv/samples.json', 'r') as file:
        data = json.load(file)
    return data


def home(request):
    domain = "cfd"
    length = 12
    movies = []
    status = False
    message = ""
    if request.method == 'POST':
        print(request.POST['length'])
        domain = request.POST['domain']
        length = request.POST['length']
    try:
        movies = movieList(domain, int(length))
    except Exception as err:
        message = err
        status = True

    return render(request, 'index.html', {
        "list": movies,
        "status": status,
        "message": message
    })
