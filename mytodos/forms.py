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

    description = forms.CharField(
        required=False,
        label="",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': "description",
                'rows': "4",
                'placeholder': "Enter Todo DESCRIPTION"
            }
        )
    )

    class Meta:
        model = Todo
        fields = ["title", "description"]
