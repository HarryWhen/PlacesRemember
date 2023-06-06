from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_auth
from social_django.models import UserSocialAuth

from . import models, forms


def load_user_data(request):
    user = request.user
    if not user.is_authenticated:
        return {}
    vk_account = UserSocialAuth.objects.filter(user=user, provider='vk-oauth2').first()
    if not vk_account:
        return {}
    avatar_url = vk_account.extra_data.get('photo')
    first_name = vk_account.extra_data.get('first_name')
    last_name = vk_account.extra_data.get('last_name')
    return {
        'avatar_url': avatar_url,
        'first_name': first_name,
        'last_name': last_name,
    }


def home(request):
    context = {}

    context.update(load_user_data(request))

    return render(request, 'app/home.html', context)


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

    context.update(load_user_data(request))

    place_remembers = models.PlaceRemember.objects.filter(user=request.user)
    context.update({
        'place_remembers': place_remembers
    })

    place_remember_form = forms.PlaceRememberForm()
    context.update({
        'place_remember_form': place_remember_form
    })

    return render(request, 'app/profile.html', context)
