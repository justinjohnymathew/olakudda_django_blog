from django.urls import path
from django.views.generic import ListView,DetailView
from blog.models import Article



urlpatterns=[
    path('',ListView.as_view(template_name='blog/index.html',model=Article),name='home'),
    path('book/<slug:slug>',DetailView.as_view(template_name='blog/article.html',model=Article),name='blog-detail')
    

]