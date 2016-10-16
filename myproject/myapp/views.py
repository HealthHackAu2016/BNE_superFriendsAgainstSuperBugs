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
import json


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            print('form provided')
            speciesfromform = form['species'].value()
            speciesjson = json.loads(speciesfromform)
            for key in speciesjson:
                newitem = Sample(date=form.date, hospital=form['hospital'].value(), doctor=form['doctor'].value(), gender=form['gender'].value(), age_group=form['age_group'].value(), postcode=form['postcode'].value(), country=form['country'].value(), travel_last_6_m = form['travel_last_6_m'], condition=form['condition'].value(), allergies_ab=form['allergies_ab'].value(), current_ab=form['current_ab'].value(), specie=key, strain = form['strains'].value(), resistances=form['resistances'].value())
                newitem.save()

            return JsonResponse({'result': 'saved'})
        else:
            return JsonResponse({'result': 'failed - form invalid'})
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


def samples(request):
    samples = Sample.objects.all().order_by('-id')[:10]

    if request.method == 'POST':
        last = request['POST'];
        return render(
            request,
            'samples.html',
            {'samples': samples, 'last': last}
        )
    else:
        return render(
            request,
            'samples.html',
            {'samples': samples}
        )
