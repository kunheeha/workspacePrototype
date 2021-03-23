from django import forms
from django.forms import ModelForm
from .models import Folder, File


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['name', 'desc', 'filename', 'folder']
        widgets = {
            'folder': forms.HiddenInput()
        }
