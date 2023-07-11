from django import forms

from fruitipedia_app.web.models import ProfileModel, FruitModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['image_url', 'age']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
            'age': '',
            'image_url': '',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                }
            )
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['email', 'password']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Image URL',
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            FruitModel.objects.all().delete()
        return self.instance

    class Meta:
        model = ProfileModel
        fields = ()


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': '',
            'description': '',
            'image_url': '',
            'price': '',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),
            'nutrition': forms.TextInput(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            )
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }


class DeleteFruitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }
