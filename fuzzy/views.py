from django.shortcuts import render
from django.http import HttpResponse
from .functions import return_fuzzy_message

def home(request):
    return render(request, 'fuzzy/home.html', {'message': ''})

def fuzzy(request):

    name1 = request.GET.get('name1', '')
    name2 = request.GET.get('name2', '')

    return_message = return_fuzzy_message(name1, name2)

    return render(request, 'fuzzy/home.html', {'message': return_message})
