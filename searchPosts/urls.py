from django.urls import path
from . import views

app_name = "searchPosts"
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search')
]