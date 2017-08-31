from datetime import date
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField

class EntryForm(forms.Form):
    name = forms.CharField(
        max_length=50)


class SkillForm(EntryForm):
    SKILL_LEVEL_CHOICES = (
      (1, 1),
      (2, 2),
      (3, 3),
      (4, 4),
      (5, 5)
    )
    skill_name = forms.CharField(
        max_length=50)
    skill_level = forms.IntegerField(
        min_value=1,
        max_value=5)


class PersonalForm(EntryForm):
    family_name = forms.CharField(
        max_length=50)
    given_name = forms.CharField(
        max_length=50)
    phone_number = PhoneNumberField()
    email_address = forms.EmailField(
        max_length=50)


class ActivityForm(EntryForm):
    location_city = forms.CharField(
        max_length=50)
    location_country = LazyTypedChoiceField(
        choices=countries)
    date_begin = forms.DateField()
    date_end = forms.DateField()
    description = forms.CharField(
        max_length=50)


class WorkForm(ActivityForm):
    job_title = forms.CharField(
        max_length=50)
    company_name = forms.CharField(
        max_length=50)

class EducationForm(ActivityForm):
    diploma_title = forms.CharField(
        max_length=50)
    school_name = forms.CharField(
        max_length=50)

class HobbyForm(ActivityForm):
    hobby_name = forms.CharField(
        max_length=50)
    hobby_institution = forms.CharField(
        max_length=50)
