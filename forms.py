from .models import FolderModel
from django.forms import ModelForm, TextInput


class FolderForm(ModelForm):
    class Meta:
        model = FolderModel
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название папки',
                'id': 'author-input'
            }),
        }

