from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def index(req):
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    return render(req, 'index.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post-detail.html", { "post": post })
