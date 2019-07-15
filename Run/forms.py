from django import forms
from .models import Profile,Conferences


class ProfileChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    conferences = forms.ModelMultipleChoiceField(
        queryset=Conferences.objects.all(), required=False)
