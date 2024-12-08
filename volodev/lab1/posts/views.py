from django.shortcuts import render
from .models import Post

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

from .models import Community

def communities_list(request):
    communities = Community.objects.all()
    return render(request, 'posts/communities_list.html', {'communities': communities})

def community_page(request, slug):
    community = Community.objects.get(slug=slug)
    return render(request, 'posts/community_page.html', {'community': community})
