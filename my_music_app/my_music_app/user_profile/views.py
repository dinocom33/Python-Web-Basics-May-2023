from django.shortcuts import render, redirect

from my_music_app.album.models import Album
from my_music_app.user_profile.forms import ProfileCreateForm, ProfileDeleteForm
from my_music_app.user_profile.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    albums_count = Album.objects.all().count()

    context = {
        'profile': profile,
        'albums_count': albums_count
    }

    return render(request, 'user_profile/profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'user_profile/profile-delete.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = ProfileCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'common/home-no-profile.html', context)
