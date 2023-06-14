from django.shortcuts import render, redirect

from notes_app.core.models import Profile, Note
from notes_app.forms import ProfileCreateForm, NoteCreateForm, NoteEditForm, NoteDeleteForm, ProfileDeleteForm


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile
    else:
        return None


def index(request):
    if not get_profile():
        return redirect(create_profile)

    context = {
        'profile': get_profile(),
        'notes': Note.objects.all(),
    }

    return render(request, 'common/home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = NoteCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'note/note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = NoteEditForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note/note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = NoteDeleteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note/note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }

    return render(request, 'note/note-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
        'profile': Profile.objects.first(),
    }

    return render(request, 'common/home-no-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    all_notes = Note.objects.all().count()

    context = {
        'profile': profile,
        'all_notes': all_notes,
    }

    return render(request, 'profile/profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-delete.html', context)
