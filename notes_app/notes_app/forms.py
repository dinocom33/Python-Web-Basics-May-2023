from django.forms import models

from notes_app.core.models import Profile, Note


class ProfileBseForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }


class ProfileCreateForm(ProfileBseForm):
    pass


class ProfileDeleteForm(ProfileBseForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Note.objects.all().delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class NoteBaseForm(models.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image',
        }


class NoteCreateForm(NoteBaseForm):
    pass


class NoteEditForm(NoteBaseForm):
    pass


class NoteDeleteForm(NoteBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
