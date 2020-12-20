from django.http import HttpResponse, Http404,JsonResponse
from django.shortcuts import render
from .models import Tweet
# Create your views here.

def Home(request,*args,**kwargs):  #* home page
    print(args, kwargs)
    return HttpResponse("<h1>Hello milind levi</h1>")


def Tweet_Home_Details(request,tweet_id,*args,**kwargs):
    data={
        "id":tweet_id,
    }
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content']=obj.content
        status = 200
    except:
        # raise Http404 
        data['message']="Not Found"
        status = 404
        
    return JsonResponse(data, status=status)
    
    #! return HttpResponse(f"<h1>Hellopranshu {tweet_id} , {obj.content}  </h1>")
