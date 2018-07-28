from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.post_list, name='blog'),
    path('view/<slug:slug>', views.post_detail, name='post_detail'),
]
