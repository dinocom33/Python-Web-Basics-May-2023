from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo


def index(request):
    # photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    # photos = [apply_user_liked_photo(photo) for photo in photos]
    photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            photos = photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'photos': photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context=context)


def like_photo(request, photo_id):
    # TODO fix when
    photo_likes = Like.objects.filter(photo_id=photo_id)

    if photo_likes:
        Like.objects.filter(photo_id=photo_id).delete()
    else:
        Like.objects.create(
            photo_id=photo_id,
        )

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')


def share_photo(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
