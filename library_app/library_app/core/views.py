from django.shortcuts import render, redirect

from .forms import CreateProfileForm, AddBookForm, EditBookForm, EditProfileForm, DeleteProfileForm
from .models import Profile, Book


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    books = Book.objects.all()

    if profile is None:
        return redirect('create profile')

    context = {
        'books': books,
        'profile': profile,
    }

    return render(request, 'common/home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = CreateProfileForm()

    context = {
        'profile': Profile.objects.first(),
        'form': form,
    }
    return render(request, 'common/home-no-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }

    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
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
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/delete-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = AddBookForm()

    context = {
        'form': form,
        'profile': Profile.objects.first(),
    }

    return render(request, 'book/add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = EditBookForm(instance=book)

    context = {
        'form': form,
        'profile': Profile.objects.first(),
        'book': book,
    }

    return render(request, 'book/edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get()

    context = {
        'book': book,
        'profile': Profile.objects.first(),
    }

    return render(request, 'book/book-details.html', context)


def delete_book(request):
    return redirect('index')