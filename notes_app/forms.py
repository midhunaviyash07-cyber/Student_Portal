from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Note

class NoteForm(forms.ModelForm):
    """
    Form for creating and editing notes
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title'}),
            'content': SummernoteWidget(),
        }