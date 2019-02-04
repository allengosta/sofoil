from django.db import models

# Create your models here.

class Asset(models.Model):
    class Meta():
        verbose_name = 'Месторождение'
        verbose_name_plural = 'Месторождения'

    name = models.CharField('Наименование', max_length=200)

    def __str__(self):
        return self.name


class Layer(models.Model):
    class Meta():
        verbose_name = 'Пласт'
        verbose_name_plural = 'Пласты'

    name = models.CharField('Наименование', max_length=200)
    asset = models.ForeignKey(Asset, blank=True, null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Well(models.Model):
    class Meta():
        verbose_name = 'Скважина'
        verbose_name_plural = 'Скважины'

    name = models.CharField('Наименование', max_length=200)
    X = models.FloatField('X', blank=False, null=False)
    Y = models.FloatField('Y', blank=False, null=False)
    asset = models.ForeignKey(Asset, blank=True, null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Intersection(models.Model):
    class Meta():
        verbose_name = 'Пластопересечение'
        verbose_name_plural = 'Пластопересечения'

    X = models.FloatField('X', blank=False, null=False)
    Y = models.FloatField('Y', blank=False, null=False)
    well = models.ForeignKey(Well, blank=True, null=True,
                             on_delete=models.CASCADE)

    layer = models.ForeignKey(Layer, blank=True, null=True,
                             on_delete=models.CASCADE)