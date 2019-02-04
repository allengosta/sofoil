from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views import generic
from app_test.models import Well, Intersection, Layer, Asset


# Create your views here.

class AssetView(generic.ListView):
    template_name = 'sofoil/index.html'
    context_object_name = 'asset_list'

    def get_queryset(self):
        return Asset.objects.all()


def well_func(request, pk):
    well_list = Well.objects.filter(asset=pk)
    return render(request, 'sofoil/detail.html', {'well_list': well_list})


def layer_func(request, pk):
    layer_list = Layer.objects.filter(asset=pk)
    return render(request, 'sofoil/detail2.html', {'layer_list': layer_list})


def intersection_func(request, id):
    inter_list = Intersection.objects.filter(well=id)
    return render(request, 'sofoil/results.html', {'inter_list': inter_list})
