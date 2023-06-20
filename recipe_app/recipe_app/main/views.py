from django.shortcuts import render, redirect

from recipe_app.main.forms import CreateRecipeForm, DeleteRecipeForm
from recipe_app.main.models import Recipe


def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }

    return render(request, 'common/index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'recipe/create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CreateRecipeForm(instance=recipe)
    else:
        form = CreateRecipeForm(request.POST, instance=recipe)
        if form .is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipe/edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipe/delete.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    context = {
        'recipe': recipe
    }

    return render(request, 'recipe/details.html', context)
