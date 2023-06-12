from django.shortcuts import render, redirect

from my_plant_app.core.forms import CreateProfileForm, CreatePlantForm, DeletePlantForm, EditPlantForm, EditProfileForm, \
    ProfileDeleteForm
from my_plant_app.core.models import Profile, Plant


def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }
    return render(request, 'common/home-page.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    number_of_plants = Plant.objects.all().count()

    context = {
        'profile': profile,
        'number_of_plants': number_of_plants,
    }
    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)


def catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants,
        'profile': Profile.objects.first()
    }

    return render(request, 'plant/catalogue.html', context)


def create_plant(request):
    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreatePlantForm()

    context = {
        'form': form,
        'profile': Profile.objects.first()
    }
    return render(request, 'plant/create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant,
        'profile': Profile.objects.first()
    }

    return render(request, 'plant/plant-details.html', context)


def edit_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditPlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
        'profile': Profile.objects.first()
    }
    return render(request, 'plant/edit-plant.html', context)


def delete_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = DeletePlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
        'profile': Profile.objects.first()
    }

    return render(request, 'plant/delete-plant.html', context)
