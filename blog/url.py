from django.urls import path
from . import views

urlpatterns = [    
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]