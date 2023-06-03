from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_auth
from social_django.models import UserSocialAuth

from . import models, forms


def home(request):
    return render(request, 'app/home.html')


@login_required(redirect_field_name=None, login_url='/')
def logout(request):
    logout_auth(request)
    return redirect('app:home')


@login_required
def profile(request):
    if request.method == 'POST':
        place_remember_form = forms.PlaceRememberForm(request.POST)
        if place_remember_form.is_valid():
            place_remember = place_remember_form.save(commit=False)
            place_remember.user = request.user
            place_remember.save()
            return redirect('app:profile')

    context = {}

    if request.user.social_auth.filter(provider='vk-oauth2').exists():
        user_social_auth = UserSocialAuth.objects.filter(provider='vk-oauth2', user=request.user).first()
        avatar_url = user_social_auth.extra_data.get('photo_big', '')
        context.update({
            'avatar_url': avatar_url
        })

    place_remembers = models.PlaceRemember.objects.filter(user=request.user)
    context.update({
        'place_remembers': place_remembers
    })

    place_remember_form = forms.PlaceRememberForm()
    context.update({
        'place_remember_form': place_remember_form
    })

    return render(request, 'app/profile.html', context)
