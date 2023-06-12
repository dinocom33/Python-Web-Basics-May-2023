from django.shortcuts import render, redirect

from games_play_app.core.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from games_play_app.core.models import Profile, Game


def index(request):
    context = {
        'profile': Profile.objects.first(),
    }
    return render(request, 'common/home-page.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'profile': Profile.objects.first(),
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    total_games = Game.objects.all().count()
    games = Game.objects.all()
    if total_games == 0:
        average_rating = 0.0
    else:
        average_rating = sum(g.rating for g in games) / total_games

    context = {
        'profile': profile,
        'total_games': total_games,
        'average_rating': average_rating,
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)


def dashboard(request):
    games = Game.objects.all()

    context = {
        'games': games,
        'profile': Profile.objects.all(),
    }

    return render(request, 'common/dashboard.html', context)


def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = CreateGameForm()

    context = {
        'form': form,
        'profile': Profile.objects.first(),
    }

    return render(request, 'game/create-game.html', context)


def game_details(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'game': game,
        'profile': Profile.objects.first(),
    }

    return render(request, 'game/details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = EditGameForm(instance=game)
    context = {
        'game': game,
        'form': form,
        'profile': Profile.objects.first(),
    }

    return render(request, 'game/edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = DeleteGameForm(instance=game)

    context = {
        'game': game,
        'form': form,
        'profile': Profile.objects.first(),
    }

    return render(request, 'game/delete-game.html', context)
