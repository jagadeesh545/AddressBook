from django import forms

class ContactSearchForm(forms.Form):
    """Simple text field form to allow users to search for contacts."""
    search_name = forms.CharField(max_length=10)
