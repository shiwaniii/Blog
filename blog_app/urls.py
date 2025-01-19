from blog_app import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post-detail/<int:pk>/', views.post_detail, name='post-detail'),
    path('draft-list/<int:pk>/', views.draft_list, name='draft-list'),
    path('draft-detail/<int:pk>/', views.draft_detail, name='draft-detail'),
    path('post_create/', views.post_create, name='post-create'),
    path('post_update/<int:pk>/', views.post_update, name='post_update'),
    path('post_delete/<int:pk>/', views.post_delete, name='post_delete'),
]




