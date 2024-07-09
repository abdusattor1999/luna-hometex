from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and not email.strip():  # Check for empty spaces
            raise forms.ValidationError('Please enter a valid email address.')
        return email