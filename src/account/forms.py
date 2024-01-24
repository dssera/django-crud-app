from django import forms

class LoginForm(forms.Form):
    # here I can put some validations on forms level
    username = forms.CharField(max_length=25)
    # + I can tell django how to render my form
    password = forms.CharField(widget=forms.PasswordInput)