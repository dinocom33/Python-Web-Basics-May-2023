from django.shortcuts import render, redirect

from my_music_app.album.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from my_music_app.album.models import Album


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album
    }

    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/delete-album.html', context)
