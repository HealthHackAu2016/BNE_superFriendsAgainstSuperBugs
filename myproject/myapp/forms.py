# -*- coding: utf-8 -*-

from django import forms
import datetime
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField


now = datetime.datetime.now().strftime("%Y-%m-%d")

GENDER_CHOICES = (('1', 'Male',), ('2', 'Female',))
AGE_CHOICES = (('1', '0-5',), ('2', '6-10',), ('3', '11-15',), ('4', '16-20',), ('5', '21-25',), ('6', '26-30',), ('7', '31-35',), ('8', '36-40',), ('9', '41-45',), ('10', '46-50',), ('11', '51-55',), ('12', '56-60',), ('13', '61-65',), ('14', '66-70',), ('15', '71-75',), ('16', '76-80',), ('17', '80+',))
AB_OPTIONS = (('Aminocoumarin', 'Aminocoumarin'), ('Aminoglycoside', 'Aminoglycoside'), ('Beta_lactamase', 'Beta_lactamase'), ('Beta_lactamase_class_A', 'Beta_lactamase_class_A'), ('Beta_lactamase_class_B', 'Beta_lactamase_class_B'), ('Beta_lactamase_class_C', 'Beta_lactamase_class_C'), ('Beta_lactamase_class_D', 'Beta_lactamase_class_D'), ('Bleomycin', 'Bleomycin'), ('Chloramphenicol', 'Chloramphenicol'), ('Cycloserine', 'Cycloserine'), ('Aminoglycoside_daptomycin', 'Aminoglycoside_daptomycin'), ('Elfamycin', 'Elfamycin'), ('Ethambutol', 'Ethambutol'), ('Fluoroquinolone', 'Fluoroquinolone'), ('Fosfomycin', 'Fosfomycin'), ('FusidicAcid', 'FusidicAcid'), ('Lincosamide', 'Lincosamide'), ('Macrolide', 'Macrolide'), ('Penicillin', 'Penicillin'), ('Polymyxin', 'Polymyxin'), ('Rifampin', 'Rifampin'), ('Rifamycin', 'Rifamycin'), ('Streptothricin', 'Streptothricin'), ('Sulfonamide', 'Sulfonamide'), ('Tetracycline', 'Tetracycline'), ('Trimethoprim', 'Trimethoprim'), ('Tunicamycin', 'Tunicamycin'), ('Aminoglycoside_vancomycin', 'Aminoglycoside_vancomycin'), ('Viomycin', 'Viomycin'))


class PatientForm(forms.Form):
    date = now
    hospital = forms.CharField(widget=forms.TextInput, label='Hospital:', max_length=15)
    doctor = forms.CharField(widget=forms.TextInput, label='Doctor:', max_length=25)
    gender = forms.ChoiceField(widget=forms.RadioSelect, label='Gender:', choices=GENDER_CHOICES)
    age_group = forms.ChoiceField(widget=forms.Select, label='Age group:', choices=AGE_CHOICES)
    postcode = forms.CharField(label='Postcode:', widget=forms.TextInput(attrs={'type':'number'}))
    country = LazyTypedChoiceField(label='Country:', choices=countries)
    travel_last_6_m = LazyTypedChoiceField(label='Traveled within last 6 months?', choices=countries)
    condition = forms.CharField(label='Condition:', widget=forms.Textarea)
    allergies_ab = forms.MultipleChoiceField(label='Allergies AB:', widget=forms.CheckboxSelectMultiple, choices=AB_OPTIONS)
    current_ab = forms.MultipleChoiceField(label='Current AB:', widget=forms.CheckboxSelectMultiple, choices=AB_OPTIONS)
    species = forms.CharField(widget=forms.HiddenInput())
    strains = forms.CharField(widget=forms.HiddenInput())
    resistances = forms.CharField(widget=forms.HiddenInput())
f = PatientForm(auto_id=True)
print(f)