from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cartoon, Category, Episode, ImageCartoon

# Create your views here.
def index(request):
    cartoons = Cartoon.objects.all()
    return render(request,'index.html', {'cartoons': cartoons})

def filterByCate(request, cate):
    category = get_object_or_404(Category, cate_name = cate)
    cartoons = Cartoon.objects.filter(cate_id = category.id)
    return render(request,'index.html', {'cartoons': cartoons})
 

def manga(request):
    return HttpResponse("hello")


def detail_view(request, id):
    episodes = Episode.objects.filter(cartoon_id = id)
    return render(request,'detail.html', {'episodes': episodes})

def detailEpisode(request, id):
    images = ImageCartoon.objects.filter(episode_id = id)
    return render(request,'detail_ep.html', {'images': images})
