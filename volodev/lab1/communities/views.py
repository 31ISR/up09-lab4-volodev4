from django.shortcuts import render
from .models import Community

def communities_list(req):
    return render(req, 'Community/communities_list.html')

def communities_list(request):
    communities = Community.objects.all()
    return render(request, 'Community/communities_list.html', {'communities': communities})

def community_page(request, slug):
    community = Community.objects.get(slug=slug)
    return render(request, 'Community/community_page.html', {'community': community})