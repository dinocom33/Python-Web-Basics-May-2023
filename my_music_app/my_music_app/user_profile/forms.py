from django import forms

from my_music_app.album.models import Album
from my_music_app.user_profile.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(forms.ModelForm):

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Album.objects.all().delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()
