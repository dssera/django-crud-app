from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    # here I can put some validations on forms level
    username = forms.CharField(max_length=25)
    # + I can tell django how to render my form
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    # these fields are additional
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password",
                               widget=forms.PasswordInput)

    class Meta:
        model = User
        # we don't want to take all fields from User model
        # btw we have uniqueness validation (for username) if we set model as User
        fields = ['username', 'first_name', 'email']


#     You can provide a clean_<fieldname>() method to
# any of your form fields in order to clean the value or raise form validation errors for a specific field.
        # this func will be executed when .is_valid() will be called
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    