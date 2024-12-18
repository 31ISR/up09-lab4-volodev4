from django.shortcuts import render
from .models import Communitie
from django.contrib.auth.decorators import login_required
from . import forms

def communities_list(request):
    communities = Communitie.objects.all().order_by('-date')
    return render(request, 'Communities/communities_list.html', {'communities': communities})

def communitie_page(request, slug):
    communities = Communitie.objects.get(slug=slug)
    return render(request, 'communities/communitie_page.html', {'communitie': communities})

@login_required(login_url="/users/login/")
def communitie_new(request):
    if request.method == 'POST': 
        form = forms.CreateCommunitie(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user 
            newpost.save()
            return redirect('communities:list')
    else:
        form = forms.CreateCommunitie()
    return render(request, 'communities/communitie_new.html', { 'form': form })