from django import forms
from django.utils.html import mark_safe
from django_countries.widgets import CountrySelectWidget

class EmailWidget(forms.widgets.TextInput):
    def render(self, name, value, attrs=None):
        attrs['class'] = "form-control"
        attrs['placeholder'] = "Email address"
        html = super(EmailWidget, self).render(name, value, attrs)
        html = '''
        <div class="input-group col-xs-6">
        <span class="input-group-addon">
          <i class="fa fa-envelope"></i>
        </span>
        ''' + html + '</div>'
        return mark_safe(html)


class TextWidget(forms.widgets.TextInput):
    def render(self, name, value, attrs=None):
        attrs['class'] = "form-control"
        attrs['placeholder'] = name
        html = super(TextWidget, self).render(name, value, attrs)
        html = '''
        <div class="input-group col-xs-6">
        ''' + html + '</div>'
        return mark_safe(html)

class PhoneWidget(forms.widgets.TextInput):
    def render(self, name, value, attrs=None):
        attrs['class'] = "form-control"
        attrs['placeholder'] = "international format phone number"
        html = super(PhoneWidget, self).render(name, value, attrs)
        html = '''
        <div class="input-group col-xs-6">
        <span class="input-group-addon">
            <i class="fa fa-phone"></i>
        </span>
        ''' + html + '</div>'
        return mark_safe(html)


class DatePickerWidget(forms.widgets.TextInput):
    def render(self, name, value, attrs=None):
        attrs['class'] = "form-control pull-right"
        attrs['placeholder'] = "yyyy/mm/dd"
        attrs['id'] = "datepicker"
        html = super(DatePickerWidget, self).render(name, value, attrs)
        html = '''
        <div class="input-group date col-xs-4">
        <span class="input-group-addon">
          <i class="fa fa-calendar"></i>
        </span>
        ''' + html
        html = html + '''
        </div>
        '''
        return mark_safe(html)

class CountryPickerWidget(CountrySelectWidget):

    def render(self, name, value, attrs=None):
        attrs['class'] = "form-control"
        html = super(CountryPickerWidget, self).render(name, value, attrs)
        return mark_safe(html)

class SkillLevelWidget(forms.RadioSelect):
    def render(self, name, value, attrs=None):
        attrs['class'] = "form-control"
        html = super(SkillLevelWidget, self).render(name, value, attrs)
        html = '''
        <div class="input-group">
        ''' + html + '</div>'
        return mark_safe(html)
