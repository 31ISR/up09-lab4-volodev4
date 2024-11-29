from django.urls import path
from .views import communities_view

urlpatterns = [
    path('', communities_view, name='communities'),
]
