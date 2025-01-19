from django.shortcuts import render, redirect
from blog_app.models import Post
from blog_app.forms import PostForm

from django.contrib.auth.decorators import login_required



# Create your views here.

def post_detail(request, pk):
    post = Post.objects.get(pk=pk, published_at__isnull=False)
    return render(request, "post_detail.html", {"post": post})


def post_list(request):
    post = Post.objects.filter(published_at__isnull=False).order_by("-published_at") #Show only publish data
    return render(request, "post_list.html", {"post":   post})

@login_required
def draft_list(request, pk):
    post = Post.objects.filter(id=pk, published_at__isnull=True)
    return render(request, "post_detail.html", {"post": post})

@login_required
def draft_detail(request, pk):
    post = Post.objects.get(id=pk,published_at__isnull=True).order_by("-published_at") #Show only publish data
    return render(request, "about.html", {"post": post})

@login_required
def post_create(request):
    if request.method == "GET":
        form = PostForm()
        return render(
            request,
            "post_create.html",
            {"form": form},
        )
    else:
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # logged in user will be the author
            post.save()
            return redirect("draft-detail", pk=post.pk)
        else:
            return render(
                request,
                "post_create.html",
                {"form": form},
            )


@login_required
def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            if post.published_at:
                return redirect("post-detail", post.pk)
            else:
                return redirect("draft-detail", post.pk)

    return render(
        request,
        "post_create.html",
        {"form": form},
    )

@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect("post-list")