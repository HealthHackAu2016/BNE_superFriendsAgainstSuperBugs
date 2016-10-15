# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Sample
from myproject.myapp.forms import PatientForm
from django.http import JsonResponse
import os
import csv


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = PatientForm(request.POST)
        #if form.is_valid():
        print('form provided')
        print(form)
        for key in form.species:
            newitem = Sample(date=form.date, hospital=form.hospital, doctor=form.doctor, gender=form.gender, age_group=form.age_group, postcode=form.postcode, country=form.country, travel_last_6_m = form.travel_last_6_m, condition = form.condition, allergies_ab = form.allergies_ab, current_ab = form.current_ab, specie = key, strain = form.strains, resistances = form.resistances)
            newitem.save()

        return JsonResponse({'result': 'saved'})
    else:
        form = PatientForm()  # A empty, unbound form

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'form': form}
    )



def getfromfile(request):
    cwd = os.getcwd()

    species = {}
    strains = []
    resistances = []

    if request.method == 'GET':
        with open('myproject/data/species.dat', 'rb') as tsvin:
            tsvin = csv.reader(tsvin, delimiter='\t')
            for row in tsvin:
                if len(row) == 9 and (row[0] != 'time'):# and ((1 - 0.5 * float(row[6])) > 0.95):
                    species[row[4]] = row[5] + ' ' + str(1 - 0.5 * float(row[6]))

        with open('myproject/data/strain.dat', 'rb') as tsvin:
            tsvin = csv.reader(tsvin, delimiter='\t')
            for row in tsvin:
                if len(row) == 9 and (row[0] != 'time') and (float(row[5]) > 0.99):
                    if not strains.__contains__(row[4]):
                        strains.append(row[4])

        with open('myproject/data/RG.dat', 'rb') as tsvin:
            tsvin = csv.reader(tsvin, delimiter='\t')
            for row in tsvin:
                if len(row) == 7 and (row[0][:2] != '##'):
                    if not resistances.__contains__(row[6]):
                        resistances.append(row[6])

        return JsonResponse({'species': species, 'strains': strains, 'resistances': resistances})


def records(request):
    samples = Sample.objects.get()

    return render(
        request,
        'samples.html',
        {'samples': samples}
    )
