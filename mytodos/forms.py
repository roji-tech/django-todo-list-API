from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        max_length=60, label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Todo TITLE',
                'aria-label': 'Todo'
            }
        ))

    class Meta:
        model = Todo
        fields = ["title"]
