from django import forms

from my_plant_app.core.models import Profile, Plant


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name')
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ('username', 'first_name', 'last_name', 'profile_image_url')
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image_url': 'Profile Picture',
        }


class ProfileDeleteForm(forms.ModelForm):

    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_type': 'Type',
            'plant_name': 'Name',
            'plant_image_url': 'Image URL',
            'plant_description': 'Description',
            'price': 'Price',
        }


class CreatePlantForm(BasePlantForm):
    pass


class PlantDetailsForm(BasePlantForm):
    pass


class EditPlantForm(BasePlantForm):
    pass


class DeletePlantForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
