from django import forms

from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['full_link']
        labels = {'full_link':'Your link:'}