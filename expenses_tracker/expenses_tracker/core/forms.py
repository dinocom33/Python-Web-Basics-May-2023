import os

from django import forms

from expenses_tracker.core.models import Profile, Expense


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileViewForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(forms.ModelForm):

    def save(self, commit=True):
        if commit:
            image_path = self.instance.profile_image.path
            Expense.objects.all().delete()
            self.instance.delete()
            os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class ExpenseBaseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('titles', 'description', 'expense_image', 'price')


class ExpenseViewForm(ExpenseBaseForm):
    pass


class CreateExpenseForm(ExpenseBaseForm):
    pass


class ExpenseEditForm(ExpenseBaseForm):
    pass


class ExpenseDeleteForm(ExpenseBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
