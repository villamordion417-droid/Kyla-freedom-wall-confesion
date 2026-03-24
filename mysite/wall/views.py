from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CustomAuthenticationForm, CustomUserCreationForm, PostForm
from .models import Post


def landing_view(request):
    return render(request, 'wall/landing.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/upload/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'wall/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/upload/')
    else:
        form = CustomAuthenticationForm(request)
    return render(request, 'wall/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def upload_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Freedom thought posted successfully.')
            return redirect('/wall/')
    else:
        form = PostForm()
    return render(request, 'wall/upload.html', {'form': form})


def wall_view(request):
    posts = Post.objects.select_related('user').all()
    return render(request, 'wall/wall.html', {'posts': posts})


@require_POST
def light_candle(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.candle_count += 1
    post.save(update_fields=['candle_count'])
    return JsonResponse({'candle_count': post.candle_count})
