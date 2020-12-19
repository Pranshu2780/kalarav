from django.http import HttpResponse, Http404,JsonResponse
from django.shortcuts import render
from .models import Tweet
# Create your views here.

def Home(request,*args,**kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello milind levi</h1>")


def Tweet_Home_Details(request,tweet_id,*args,**kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    data={
        "id":tweet_id,
        "content":obj.content,
        # "image_path":obj.image.url
    }
    return JsonResponse()
    return HttpResponse(f"<h1>Hellopranshu {tweet_id} , {obj.content}  </h1>")
