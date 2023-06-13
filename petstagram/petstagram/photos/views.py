from django.shortcuts import render, redirect

from .forms import PhotoCreateForm, PhotoEditForm
from .models import Photo


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context=context)


def edit_photo(request, pk):
    form = PhotoEditForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('details photo')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-edit-page.html', context=context)


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comments_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }

    return render(request, 'photos/photo-details-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')
