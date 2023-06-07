from django.shortcuts import render, redirect

from car_collection.web.forms import ProfileCreateForm, CarCreateForm, CarDetailsForm, CarDeleteForm, \
    ProfileDetailsForm, ProfileEditForm, ProfileDeleteForm
from car_collection.web.models import Car, Profile


def get_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist:
        return None


def index(request):

    context = {
        'profile': Profile.objects.first()
    }

    return render(request, 'common/index.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    profile = Profile.objects.get()
    cars = Car.objects.all()
    total_price = sum(c.price for c in cars)

    context = {
        'profile': profile,
        'total_price': total_price,
        'car': Car.objects.first(),
    }

    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-delete.html', context)


def catalogue(request):
    cars = Car.objects.all()
    profile = Profile.objects.get()
    total_cars = len(cars)

    context = {
        'cars': cars,
        'profile': profile,
        'total_cars': total_cars,
    }

    return render(request, 'car/catalogue.html', context)


def create_car(request):
    if request.method == 'POST':
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarCreateForm()

    context = {
        'form': form,
        'profile': Profile.objects.first()
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarDetailsForm(instance=car)
    else:
        form = CarDetailsForm(request.POST, instance=car)

    context = {
        'form': form,
        'car': car,
        'profile': Profile.objects.first()
    }

    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = CarDetailsForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarDetailsForm(instance=car)

    context = {
        'form': form,
        'car': car,
        'profile': Profile.objects.first()
    }

    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarDeleteForm(instance=car)

    context = {
        'form': form,
        'car': car,
        'profile': Profile.objects.first()
    }

    return render(request, 'car/car-delete.html', context)
