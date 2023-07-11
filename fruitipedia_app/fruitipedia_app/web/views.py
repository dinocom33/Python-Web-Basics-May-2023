from django.shortcuts import render, redirect

from fruitipedia_app.web.forms import CreateProfileForm, CreateFruitForm, EditFruitForm, DeleteFruitForm, \
    EditProfileForm, DeleteProfileForm
from fruitipedia_app.web.models import FruitModel, ProfileModel


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = FruitModel.objects.all()

    context = {
        'fruits': fruits,
    }

    return render(request, 'common/dashboard.html', context)


def create_fruit(request):
    if request.method == 'GET':
        form = CreateFruitForm()
    else:
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()

    context = {
        'fruit': fruit
    }

    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'fruit': fruit
    }

    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteFruitForm(instance=fruit)
    else:
        form = DeleteFruitForm(request.POST,instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruit/delete-fruit.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'user_profile/create-profile.html', context)


def details_profile(request):
    profile = ProfileModel.objects.first()
    fruits_count = FruitModel.objects.all().count()

    context = {
        'profile': profile,
        'fruits_count': fruits_count,
    }

    return render(request, 'user_profile/details-profile.html', context)


def edit_profile(request):
    profile = ProfileModel.objects.first()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'user_profile/edit-profile.html', context)


def delete_profile(request):
    profile = ProfileModel.objects.first()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'user_profile/delete-profile.html', context)
