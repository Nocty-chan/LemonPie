from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from ..models import (
    CVEntry,
)
from ..forms import (
    SkillForm,
    PersonalForm,
    WorkForm,
    EducationForm,
    HobbyForm,
)

def modify_skill(request, entry_id):
    cv_entry = get_object_or_404(CVEntry, pk=entry_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SkillForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cv_entry.name = form.cleaned_data['name']
            cv_entry.skill_name = form.cleaned_data['skill_name']
            cv_entry.skill_level = form.cleaned_data['skill_level']
            cv_entry.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('resumebuilder:all_entrys', args=()))
    # if a GET (or any other method) we'll create a blank form
    else:
        context = {
            'cv_entry': cv_entry,
            'enable_modification': True,
        }
        return render(request, 'form.html', context)


def modify_personal(request, entry_id):
    cv_entry = get_object_or_404(CVEntry, pk=entry_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cv_entry.name = form.cleaned_data['name']
            cv_entry.family_name = form.cleaned_data['family_name']
            cv_entry.given_name = form.cleaned_data['given_name']
            cv_entry.phone_number = form.cleaned_data['phone_number']
            cv_entry.email_address = form.cleaned_data['email_address']
            cv_entry.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('resumebuilder:all_entrys', args=()))
        else:
            context = {
                'cv_entry': cv_entry,
                'enable_modification': True,
            }
            return render(request, 'form.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        context = {
            'cv_entry': cv_entry,
            'enable_modification': True,
        }
        return render(request, 'form.html', context)


def process_activity_part(cv_entry, form):
    cv_entry.name = form.cleaned_data['name']
    cv_entry.location_city = form.cleaned_data['location_city']
    cv_entry.location_country = form.cleaned_data['location_country']
    cv_entry.date_begin = form.cleaned_data['date_begin']
    cv_entry.date_end = form.cleaned_data['date_end']
    cv_entry.description = form.cleaned_data['description']
    return cv_entry

def modify_job(request, entry_id):
    cv_entry = get_object_or_404(CVEntry, pk=entry_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cv_entry = process_activity_part(cv_entry, form)
            cv_entry.job_title = form.cleaned_data['job_title']
            cv_entry.company_name = form.cleaned_data['company_name']
            cv_entry.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('resumebuilder:all_entrys', args=()))
        else:
            context = {
                'cv_entry': cv_entry,
                'enable_modification': True,
            }
            return render(request, 'form.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        context = {
            'cv_entry': cv_entry,
            'enable_modification': True,
        }
        return render(request, 'form.html', context)

def modify_education(request, entry_id):
    cv_entry = get_object_or_404(CVEntry, pk=entry_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EducationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cv_entry = process_activity_part(cv_entry, form)
            cv_entry.diploma_title = form.cleaned_data['diploma_title']
            cv_entry.school_name = form.cleaned_data['school_name']
            cv_entry.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('resumebuilder:all_entrys', args=()))
        else:
            context = {
                'cv_entry': cv_entry,
                'enable_modification': True,
            }
            return render(request, 'form.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        context = {
            'cv_entry': cv_entry,
            'enable_modification': True,
        }
        return render(request, 'form.html', context)

def modify_hobby(request, entry_id):
    cv_entry = get_object_or_404(CVEntry, pk=entry_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HobbyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cv_entry = process_activity_part(cv_entry, form)
            cv_entry.hobby_name = form.cleaned_data['hobby_name']
            cv_entry.hobby_institution = form.cleaned_data['hobby_institution']
            cv_entry.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('resumebuilder:all_entrys', args=()))
        else:
            context = {
                'cv_entry': cv_entry,
                'enable_modification': True,
            }
            return render(request, 'form.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        context = {
            'cv_entry': cv_entry,
            'enable_modification': True,
        }
        return render(request, 'form.html', context)
