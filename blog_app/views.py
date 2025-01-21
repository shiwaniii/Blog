from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.utils import timezone

from blog_app.forms import PostForm
from blog_app.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = "posts"

    def get_queryset(self):
     posts = Post.objects.filter(published_at__isnull=False).order_by("-id")
     return posts
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "posts"

    def get_queryset(self):
     queryset = Post.objects.filter(pk=self.kwargs["pk"], published_at__isnull=False)
     return queryset
    
class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'draft_list.html'
    context_object_name = "posts"

    def get_queryset(self):
     queryset = Post.objects.filter(published_at__isnull=True)
     return queryset
    
class DraftDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'draft_detail.html'
    context_object_name = "posts"

    def get_queryset(self):
     queryset = Post.objects.filter(published_at__isnull=True)
     return queryset
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = reverse_lazy("draft-list")

    def form_valid(self, form):
     form.instance.author = self.request.user
     return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
   

    def get_success_url(self):
     post = self.get_object()
     if post.publishedat:
        return reverse_lazy("post-detail", kwargs={"pk": post.pk})
     else:
        return reverse_lazy("draft-detail", kwargs={"pk": post.pk})
     

class PostDeleteView(LoginRequiredMixin, View):
   def get(self, request, pk):
      post = Post.objects.get(pk=pk)
      post.delete()
      return redirect("post-list")
   

class PostPublishView(LoginRequiredMixin, View):
    def post(self, request, pk):
       post = Post.objects.get(pk=pk, published_at__isnull =True)
       post.published_at = timezone.now()
       post.save()
       return redirect("post-list")
   


   
    


