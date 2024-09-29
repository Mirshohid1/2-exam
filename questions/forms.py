from django import forms
from .models import Questions

class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter a your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter a your email'}),
            'text': forms.Textarea(attrs={'placeholder': 'Enter a your question'})
        }