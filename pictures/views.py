from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404


# Create your views here.
def index(request):
    return render(request, 'index.html')

def latest_images(request):
    date = dt.date.today()
    images = Image.latest_images()
    return render (request, 'index.html', {"date": date, "news": news })