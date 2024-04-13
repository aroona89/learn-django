from django.shortcuts import render
from travello.models import Destination

# Create your views here.

def index(request):
    DestinationData =  Destination.objects.all()
    data = {
        'DestinationData' : DestinationData
    }
    return render(request, "index.html", data)