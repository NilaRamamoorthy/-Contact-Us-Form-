from django import forms
from .models import ContactSubmission

# Optional: ModelForm
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']
