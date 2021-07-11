from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
@login_required
def index(request):
    return render(request, 'front/render/index.html')

@login_required
def api_keys(request):
    return render(request, 'front/render/api_keys.html')

def login_form(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('front:index'))
    
    if request.method == "POST":
        ...
    else:
        return render(request, 'front/render/login.html')

def register_form(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('front:index'))
    
    if request.method == "POST":
        ...
    else:
        return render(request, 'front/render/register.html')