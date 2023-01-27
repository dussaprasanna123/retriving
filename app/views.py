from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    QST=Topic.objects.all()
    d={'ts':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='volley ball')
    QSW=Webpage.objects.exclude(topic_name='volley ball')
    webpages=Webpage.objects.all().order_by('name')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())

    d={'dl':QSW}
    return render(request,'display_webpage.html',d)