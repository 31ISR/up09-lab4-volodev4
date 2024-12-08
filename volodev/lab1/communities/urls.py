from django.urls import path
from . import views 

app_name = 'communities'

urlpatterns = [
    path('', views.communities_list),
    path('', views.communities_list, name="communities"),
    path('<slug:slug>/', views.post_page, name="page"),

]



communities