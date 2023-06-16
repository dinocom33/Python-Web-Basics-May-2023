from django.shortcuts import render, redirect

from .templatetags import get_profile
from ..album.models import Album
from ..user_profile.models import Profile


def index(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()

    if not profile:
        return redirect('create profile')

    context = {
        'albums': albums,
    }

    return render(request, 'common/home-with-profile.html', context)
