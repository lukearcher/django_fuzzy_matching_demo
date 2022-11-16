from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'fuzzy/home.html', {'message': ''})

def fuzzy(request):

    #sentiment_phrase = request.GET.get('phrase', '')

    return_message = 'Fuzzy Matching Results: '

    return render(request, 'fuzzy/home.html', {'message': return_message})
