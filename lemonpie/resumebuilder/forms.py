from datetime import date
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from .widgets import EmailWidget, TextWidget, DatePickerWidget

class EntryForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=TextWidget)


class SkillForm(EntryForm):
    skill_name = forms.CharField(
        max_length=50,
        widget=TextWidget)
    skill_level = forms.IntegerField(min_value=1, max_value=5)


class PersonalForm(EntryForm):
    family_name = forms.CharField(
        max_length=50,
        widget=TextWidget)
    given_name = forms.CharField(
        max_length=50,
        widget=TextWidget)
    phone_number = PhoneNumberField()
    email_address = forms.EmailField(
        max_length=50,
        widget=EmailWidget)


class ActivityForm(EntryForm):
    location_city = forms.CharField(
        max_length=50,
        widget=TextWidget)
    location_country = LazyTypedChoiceField(choices=countries)
    #TODO: Add a widget for Date selection
    date_begin = forms.DateField(
      widget=DatePickerWidget
    )
    date_end = forms.DateField(
      widget=DatePickerWidget
    )
    description = forms.CharField(
        max_length=50,
        widget=forms.Textarea(
            attrs={
              'class': "form-control"
            }
        ))


class WorkForm(ActivityForm):
    job_title = forms.CharField(
        max_length=50,
        widget=TextWidget)
    company_name = forms.CharField(
        max_length=50,
        widget=TextWidget)

class EducationForm(ActivityForm):
    diploma_title = forms.CharField(
        max_length=50,
        widget=TextWidget)
    school_name = forms.CharField(
        max_length=50,
        widget=TextWidget)

class HobbyForm(ActivityForm):
    hobby_name = forms.CharField(
        max_length=50,
        widget=TextWidget)
    hobby_institution = forms.CharField(
        max_length=50,
        widget=TextWidget)
