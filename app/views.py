from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_auth
from social_django.models import UserSocialAuth


def home(request):
    return render(request, 'app/home_page.html')


@login_required
def logout(request):
    logout_auth(request)
    return redirect('app:home')


@login_required
def profile(request):
    context = {}

    if request.user.social_auth.filter(provider='vk-oauth2').exists():
        user_social_auth = UserSocialAuth.objects.filter(provider='vk-oauth2', user=request.user).first()
        avatar_url = user_social_auth.extra_data.get('photo_big', '')
        context.update({
            'avatar_url': avatar_url
        })

    return render(request, 'app/profile_page.html', context)
