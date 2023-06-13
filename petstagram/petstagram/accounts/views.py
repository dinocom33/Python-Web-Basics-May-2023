from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from petstagram.accounts.forms import UserRegistrationForm


def login_user(request):
    return render(request, 'accounts/login-page.html')


def register_user(request):
    form = UserRegistrationForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('login user')

    context = {
        'form': form,
    }
    return render(request, 'accounts/register-page.html', context=context)


def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')
