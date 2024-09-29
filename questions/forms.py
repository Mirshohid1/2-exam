from django import forms
from .models import Questions

class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'placeholder': 'Enter your question', 'class': 'form-control'}),
        }