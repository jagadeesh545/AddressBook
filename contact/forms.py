from django import forms

class ContactSearchForm(forms.Form):
    search_name = forms.CharField(max_length=10)
