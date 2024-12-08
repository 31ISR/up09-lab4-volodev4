from django.urls import path
from . import views 

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('<slug:slug>/', views.post_page, name="page"),
    path('communities/', views.communities_list, name="communities"),  
    path('communities/<slug:slug>/', views.community_page, name="community"),
]
