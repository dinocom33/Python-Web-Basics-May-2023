from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from pyperclip import copy

from petstagram.common.models import Like
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo


def index(request):
    # photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    # photos = [apply_user_liked_photo(photo) for photo in photos]
    photos = Photo.objects.all()

    context = {
        'photos': photos,
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
    # photo_details_url = reverse('details photo', kwargs={
    #     'pk': photo_id
    # })
    # copy(photo_details_url)
    copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')
