from django.shortcuts import render

# Create your views here.

def index(request):


    return render(request, 'index.html', {})


def linechart(request):

    return render(request, 'linechart.html', {})
