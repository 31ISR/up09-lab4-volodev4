from django.urls import path
from . import views 

app_name = 'page'

urlpatterns = [
    path('', views.communities_list),
    path('', views.communities_list, name="communities"),
    path('<slug:slug>/', views.community_page, name="page"),

]
