from django.shortcuts import render
from .models import Video
# Create your views here.

def video_list(request):
    posts = Video.objects.order_by('-youtube_likes')
    return render(request, 'video/video_list.html', {'posts': posts})


