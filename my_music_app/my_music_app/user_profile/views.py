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

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'user_profile/profile-delete.html', context)
