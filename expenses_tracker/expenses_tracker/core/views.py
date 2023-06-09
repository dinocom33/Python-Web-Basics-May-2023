from django.db.models import Sum, F
from django.shortcuts import render, redirect

from expenses_tracker.core.forms import ProfileCreateForm, ProfileViewForm, CreateExpenseForm, ExpenseEditForm, \
    ExpenseDeleteForm, ProfileEditForm, ProfileDeleteForm
from expenses_tracker.core.models import Profile, Expense


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def total_expenses():
    total = Expense.objects.aggregate(TOTAL=Sum('price'))['TOTAL']

    return total


def index(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    money_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
        'money_left': money_left,
    }

    return render(request, 'common/home-with-profile.html', context)


def create_expense(request):
    if request.method == 'GET':
        form = CreateExpenseForm()
    else:
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'expense/expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = ExpenseEditForm(instance=expense)
    else:
        form = ExpenseEditForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'expense/expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = ExpenseDeleteForm(instance=expense)
    else:
        form = ExpenseDeleteForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense/expense-delete.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = form.instance
            return redirect('index')

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'common/home-no-profile.html', context)


def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    expenses_count = len(expenses)

    context = {
        'profile': profile,
        'budget_left': budget_left,
        'expenses_count': expenses_count
    }

    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)
