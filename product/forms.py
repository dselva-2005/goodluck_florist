from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comment']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=1000)