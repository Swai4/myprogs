from django.urls import path
from . import views
from .views import PostDetailView
from blog import views as blog_views

urlpatterns = [
    path('postlist/', blog_views.postlist, name='post_list'),
    path('about/', views.about, name='blog-about'),
    path('search/', views.search, name='search'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]