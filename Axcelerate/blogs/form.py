from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        content = forms.CharField(widget=FroalaEditor)
        fields = ['title', 'content']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']
