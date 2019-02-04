from django.test import TestCase
import os, sys, django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sofoil.settings')
django.setup()

from app_test.models import Asset, Well, Layer, Intersection


# Create your tests here.


def func():
    asset, created_asset = Asset.objects.get_or_create(name='Месторождение 1')
    well1, well_created1 = Well.objects.get_or_create(asset=asset, name='Скважина 1', X=1.5, Y=1.5)
    well2, well_created2 = Well.objects.get_or_create(asset=asset, name='Скважина 2', X=2.5, Y=2.5)
    well3, well_created3 = Well.objects.get_or_create(asset=asset, name='Скважина 3', X=3.5, Y=3.5)
    well4, well_created4 = Well.objects.get_or_create(asset=asset, name='Скважина 4', X=4.5, Y=4.5)
    well5, well_created5 = Well.objects.get_or_create(asset=asset, name='Скважина 5', X=5.5, Y=5.5)

    layer1, layer_created1 = Layer.objects.get_or_create(asset=asset, name='Пласт 1')
    layer2, layer_created2 = Layer.objects.get_or_create(asset=asset, name='Пласт 2')

    inter1, created1 = Intersection.objects.get_or_create(well=well1, layer=layer1, X=1.5, Y=1.5)
    inter2, created2 = Intersection.objects.get_or_create(well=well2, layer=layer1, X=2.5, Y=2.5)
    inter3, created3 = Intersection.objects.get_or_create(well=well3, layer=layer1, X=3.5, Y=3.5)
    inter4, created4 = Intersection.objects.get_or_create(well=well4, layer=layer1, X=4.5, Y=4.5)
    inter5, created5 = Intersection.objects.get_or_create(well=well5, layer=layer1, X=5.5, Y=5.5)

    inter6, created6 = Intersection.objects.get_or_create(well=well1, layer=layer2, X=1.5, Y=1.5)
    inter7, created7 = Intersection.objects.get_or_create(well=well2, layer=layer2, X=2.5, Y=2.5)
    inter8, created8 = Intersection.objects.get_or_create(well=well3, layer=layer2, X=3.5, Y=3.5)
    inter9, created9 = Intersection.objects.get_or_create(well=well4, layer=layer2, X=4.5, Y=4.5)
    inter10, created10 = Intersection.objects.get_or_create(well=well5, layer=layer2, X=5.5, Y=5.5)


func()
