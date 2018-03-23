from django import forms


class ImageForm(forms.Form):
    img = forms.CharField(widget=forms.HiddenInput(), required=False)
