# from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'name-text', 'required': True, 'placeholder': 'Billy Bob Joe'}
            ),
            'email': forms.TextInput(
                attrs={'id': 'email-text', 'required': True, 'placeholder': '@something.com'}
            ),
            'message': forms.TextInput(
                attrs={'id': 'message-text', 'required': True, 'placeholder': 'Tell me what\'s up!'}
            ),
        }