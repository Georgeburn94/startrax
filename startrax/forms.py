# filepath: /workspace/startrax/forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['album', 'star_rating', 'note']