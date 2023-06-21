from django.shortcuts import render, redirect

from ..album.models import Album
from ..user_profile.models import Profile
from ..user_profile.forms import ProfileCreateForm


def index(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()

    if not profile:
        template = 'common/home-no-profile.html'
    else:
        template = 'common/home-with-profile.html'

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'albums': albums,
        'form': form,
    }

    return render(request, template, context)
