from asyncio.windows_events import NULL
from pickle import NONE
from django.shortcuts import render
from django.contrib import messages

import csv, io

from .models import asset, default

from .forms import AssetForm


def index(request):

    print(request.POST)
    
    if request.method == "POST":

        assetSubmission = AssetForm(request.POST, request.FILES)

        if assetSubmission.is_valid():
            
            ids = asset.objects.values_list('id', flat=True)
            for ID in ids:

                if str(ID) in request.POST:
                    edittedAsset = asset.objects.get(id=ID)

                    if assetSubmission.cleaned_data['AssetThumbnail']:
                        edittedAsset.Image = assetSubmission.cleaned_data['AssetThumbnail']
                    if assetSubmission.cleaned_data['subjectArea']:
                        edittedAsset.Area = assetSubmission.cleaned_data['subjectArea']
                    if assetSubmission.cleaned_data['assetLocation']:
                        edittedAsset.Location = assetSubmission.cleaned_data['assetLocation']
                    edittedAsset.save()
        
    assetForm = AssetForm()

    assets = asset.objects.all()

    ids = asset.objects.values_list('id', flat=True)
    for ID in ids:

        selectedAsset = asset.objects.get(id=ID)

        if not selectedAsset.Image:
            selectedAsset.Image = default.objects.get(id=1).Image
            selectedAsset.save()

    assets = asset.objects.all()

    return render(request, "Asset_manager_web_app/index.html", {'content': assets, 'assetForm': assetForm})


def import_csv(request):

    if request.method == "GET":
        return render(request, "Asset_manager_web_app/uploadCSV.html", {})

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
        return render(request, "Asset_manager_web_app/uploadCSV.html", {})

    data = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data)

    reader = csv.reader(io_string, delimiter=',')

    for row in reader:
        asset.objects.create(Name=row[0],Area=row[1],Image = default.objects.get(id=1).Image, Location = default.objects.get(id=1).Location)

    return render(request, "Asset_manager_web_app/uploadCSV.html", {})