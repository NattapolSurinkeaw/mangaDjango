from django.shortcuts import render
from django.http import HttpResponse
from .models import Cartoon

# Create your views here.
def index(request):
    cartoons = Cartoon.objects.all()
    return render(request,'index.html', {'cartoons': cartoons})

def manga(request):
    return HttpResponse("hello")


def detail_view(request):
    return HttpResponse("hello")
