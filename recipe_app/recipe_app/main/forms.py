from django import forms

from recipe_app.main.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image_url': 'Image URL',
            'ingredients': 'Ingredients',
            'time': 'Time (Minutes)',
        }


class CreateRecipeForm(RecipeBaseForm):
    pass


class EditRecipeForm(RecipeBaseForm):
    pass


class DeleteRecipeForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
