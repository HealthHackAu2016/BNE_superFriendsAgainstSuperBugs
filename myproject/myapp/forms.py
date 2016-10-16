# -*- coding: utf-8 -*-

from django import forms
import datetime
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from myproject.myapp.models import GENDER_CHOICES
from myproject.myapp.models import AGE_CHOICES
from myproject.myapp.models import AB_OPTIONS
from myproject.myapp.models import COUNTRY_OPTION


now = datetime.datetime.now().strftime("%Y-%m-%d")


class PatientForm(forms.Form):
    date = now
    hospital = forms.CharField(widget=forms.TextInput, label='Hospital:', max_length=15)
    doctor = forms.CharField(widget=forms.TextInput, label='Doctor:', max_length=25)
    gender = forms.ChoiceField(widget=forms.RadioSelect, label='Gender:', choices=GENDER_CHOICES)
    age_group = forms.ChoiceField(widget=forms.Select, label='Age group:', choices=AGE_CHOICES)
    postcode = forms.CharField(label='Postcode:', widget=forms.TextInput(attrs={'type':'number'}))
    country = forms.ChoiceField(widget=forms.Select, label='Country:', choices=COUNTRY_OPTION, initial='AU')
    travel_last_6_m = forms.ChoiceField(widget=forms.Select, label='Traveled within last 6 months?', choices=COUNTRY_OPTION)
    condition = forms.CharField(label='Condition:', widget=forms.Textarea)
    allergies_ab = forms.MultipleChoiceField(label='Allergies AB:', widget=forms.CheckboxSelectMultiple, choices=AB_OPTIONS)
    current_ab = forms.MultipleChoiceField(label='Current AB:', widget=forms.CheckboxSelectMultiple, choices=AB_OPTIONS)
    species = forms.CharField(widget=forms.HiddenInput())
    strains = forms.CharField(widget=forms.HiddenInput())
    resistances = forms.CharField(widget=forms.HiddenInput())
f = PatientForm(auto_id=True)
print(f)