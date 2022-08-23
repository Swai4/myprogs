from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='folio-index'),
    path('anim/', views.anim, name='folio-anim'),
]