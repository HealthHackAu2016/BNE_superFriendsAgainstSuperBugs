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
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            print('form provided')
            #newdoc = Document(docfile=request.FILES['docfile'])
            #newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = PatientForm()  # A empty, unbound form

    # Load documents for the list page
    #documents = Document.objects.all()

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
                    species[row[4]] = float(row[5])

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
