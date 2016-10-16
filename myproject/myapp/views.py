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
from pprint import pprint
from django.core import serializers
import unicodedata


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            print('form provided')
            speciesfromform = form['species'].value()
            speciesjson = json.loads(speciesfromform)
            for key in speciesjson:
                keywithunderscores = key.replace(" ", "_")
                for strainkey in json.loads(form['strains'].value()):
                    strainwithunderscores = strainkey.replace(" ", "_")
                    if strainwithunderscores.startswith(keywithunderscores):
                        strainalone = strainwithunderscores.replace(keywithunderscores+"_", "")
                        newitem = Sample(date=form.date, hospital=form['hospital'].value(), ward=form['ward'].value(), doctor=form['doctor'].value(), gender=form['gender'].value(), age_group=form['age_group'].value(), postcode=form['postcode'].value(), country=form['country'].value(), travel_last_6_m = form['travel_last_6_m'].value(), condition=form['condition'].value(), allergies_ab=form['allergies_ab'].value(), current_ab=form['current_ab'].value(), specie=key, strain=strainalone, resistances=form['resistances'].value())
                        newitem.save()
                        samplelist = Sample.objects.filter(doctor=form['doctor'].value()).order_by('-id')[:10]
                        pprint(vars(newitem))
                        return render(request, 'samples.html', {'samples': samplelist, 'last': newitem})

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

def getallsamples(request):
    samples = Sample.objects.all()
    samplesjson = []
    for sample in samples:
        allergies_ab = json.loads(sample.allergies_ab.replace("u\'", "\'").replace("\'","\""))
        current_ab = json.loads(sample.current_ab.replace("u\'", "\'").replace("\'","\""))
        samplejson = {'id': sample.id, 'date': sample.date, 'hospital': sample.hospital, 'ward': sample.ward, 'doctor': sample.doctor, 'gender': sample.gender, 'age_group': sample.age_group, 'postcode': sample.postcode, 'country': sample.country, 'traveled':sample.travel_last_6_m, 'condition': sample.condition, 'allergies_ab': allergies_ab, 'current_ab': current_ab, 'specie': sample.specie, 'strain': sample.strain, 'resistances': json.loads(sample.resistances)}
        samplesjson.append(samplejson)
    return JsonResponse(samplesjson, safe=False)

def deleteallsamples(request):
    Sample.objects.all().delete()
    return JsonResponse({'result': 'deleted'})

def generateinputsamples(request):
    samples = []
    with open('myproject/data/aaa.csv', 'rb') as tsvin:
            tsvin = csv.reader(tsvin, delimiter=',')
            for row in tsvin:
                if len(row) == 26:
                    print('yes')
                    date = "2016-" + row[0][:5]
                    hospital = row[1]
                    ward = row[2]
                    doctor = row[3]
                    gender = row[4]
                    age = row[5]
                    postcode = row[6]
                    country = row[7]
                    travel = row[8]
                    condition = row[9]
                    specie = row[10]
                    strain = row[11]
                    resist = []
                    if row[12] == 1:
                        resist.append("amioglycoside")
                    if row[13] == 1:
                        resist.append("beta_lactamase")
                    if row[14] == 1:
                        resist.append("beta_lactamase_class_A")
                    if row[15] == 1:
                        resist.append("beta_lactamase_class_B")
                    if row[16] == 1:
                        resist.append("beta_lactamase_class_C")
                    if row[17] == 1:
                        resist.append("beta_lactamase_class_D")
                    if row[18] == 1:
                        resist.append("chloramphenicol")
                    if row[19] == 1:
                        resist.append("fluoroquiolone")
                    if row[20] == 1:
                        resist.append("fosfomycin")
                    if row[21] == 1:
                        resist.append("penicillin")
                    if row[22] == 1:
                        resist.append("polymyxin")
                    if row[23] == 1:
                        resist.append("rifamycin")
                    if row[24] == 1:
                        resist.append("tetracycline")
                    if row[25] == 1:
                        resist.append("trimethoprim")

                    sample = Sample(current_ab="[]", allergies_ab="[]", date=date, hospital=hospital, ward=ward, doctor=doctor, gender=gender, age_group=age, postcode=postcode, country=country, travel_last_6_m=travel, condition=condition, specie=specie, strain=strain, resistances=resist)
                    sample.save()
                else:
                    print('no, ' + str(len(row)))
    return JsonResponse({'result': 'doing ...'})


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


def results(request):
    return render(
        request,
        'results.html',
        {}
    )