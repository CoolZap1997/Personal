from django import forms
from datetime import date

class UserForm(forms.Form):
    GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('O', 'Others',),
    )

    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    gender = forms.ChoiceField(label='Gender', max_length=1, choices=GENDER_CHOICES)
    country_code = forms.CharField(label='Country Code', min_length=2, max_length=4)
    phone = forms.IntegerField(label='Phone Number', max_length=10)
    email = forms.CharField(label='Email ID', max_length=50, unique=True)
    password = forms.CharField(label='Password', min_length=8, max_length=100)
    confirm_password = forms.CharField(label='Confirm Password', min_length=8, max_length=100)
    
class HabitsForm(forms.Form):
    habit = forms.CharField(max_length=30, unique=True)

class RecordsForm(forms.Form):
    record_date = forms.DateField(default=date.today)