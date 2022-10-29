from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from  .soup1tamilmv.index import  movieList
import json
def sample():
    with open('/home/varun/Desktop/tamilrockers/tamilrockers/soup1tamilmv/samples.json', 'r') as file:
        data = json.load(file)
    return data


def home(request,length):
    context = {
        # "list":sample()
        "list":movieList(length)
        
    }
    return render(request, 'index.html',context)
