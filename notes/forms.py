from django import forms
from .models import Category, Note



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text', 'reminder','category')
