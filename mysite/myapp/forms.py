from django import forms
from .models import Project
from django.core.files.storage import FileSystemStorage

class MyProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'image',
            'url',
            # 'created_at',
            # 'updated_at',
            # 'delete_at',
        )
        labels = {
            'title': 'Titulo',
            'description': 'Descripción',
            'image': 'Imagen',
            'url': 'Url',
            # 'created_at': 'Create',
            # 'updated_at': 'Update',
            # 'delete_at': 'Delete',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(),
            'url': forms.URLInput(),
            # 'created_at': forms.DateTimeInput(attrs={'class':'form-control'}),
            # 'updated_at': forms.DateTimeInput(attrs={'class':'form-control'}),
            # 'deleted_at': forms.DateTimeInput(attrs={'class':'form-control'}),
        }