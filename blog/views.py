from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def index(req):
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    return render(req, 'index.html', {'posts': posts})