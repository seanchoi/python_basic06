from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    
    GENDER = [ 
        ('male','MALE'),
        ('female','FEMALE'),
    ]
    
    first_name = forms.CharField(required = False, validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(20)])
    last_name = forms.CharField()
    email = forms.EmailField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)
    ssn = forms.IntegerField()


"""
def clean(self):
    user_cleaned_data = super().clean()
    inputFirstName = user_cleaned_data['fist_name']
    if len(inputFirstName)> 20:
        raise forms.ValidationError('Tha max length of First Name is 20 characters')


def clean_first_name(self):
    input_first_name = self.cleaned_data['fist_name']
    if len(input_first_name)> 20:
        raise forms.ValidationError('Tha max length of First Name is 20 characters')
    return input_first_name

def clean_email(self):
    input_email = self.cleaned_data['email']
    if input_email.find('@') == -1:
        raise forms.ValidationError('The email shoud contain @')
    return input_email

"""