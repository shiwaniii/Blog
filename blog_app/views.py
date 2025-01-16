from django.shortcuts import render
from blog_app.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_detail(request, pk):
    post = Post.objects.get(pk=pk, published_at__isnull=False)
    return render(request, "post_detail.html", {"post": post})


def post_list(request):
    post = Post.objects.filter(published_at__null=False).order_by("-published_at") #Show only publish data
    return render(request, "about.html", {"post": post})

@login_required
def draft_list(request):
    post = Post.objects.get(pk=pk, published_at__isnull=True)
    return render(request, "post_detail.html", {"post": post})

@login_required
def draft_list(request):
    post = Post.objects.filter(published_at__null=True).order_by("-published_at") #Show only publish data
    return render(request, "about.html", {"post": post})

