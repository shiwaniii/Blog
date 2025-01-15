from django.shortcuts import render

def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts":posts})