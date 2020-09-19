from django.shortcuts import render

# Create your views here.

def home(request):
    htmlfile = "homepage/index.html"
    return render(request, htmlfile)