from django import forms


class MountForm(forms.Form):
    mountpoint = forms.CharField(max_length=100)
