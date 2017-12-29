from django import forms

class LoginForm(forms.Form):
    access_code = forms.CharField(label='Access code', max_length=16, widget=forms.TextInput(attrs={"required": True, "class": "form-control"}))