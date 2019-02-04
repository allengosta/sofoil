# Generated by Django 2.0.10 on 2019-02-03 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'verbose_name': 'Месторождение', 'verbose_name_plural': 'Месторождения'},
        ),
        migrations.AlterModelOptions(
            name='intersection',
            options={'verbose_name': 'Пластопересечение', 'verbose_name_plural': 'Пластопересечения'},
        ),
        migrations.AlterModelOptions(
            name='layer',
            options={'verbose_name': 'Пласт', 'verbose_name_plural': 'Пласты'},
        ),
        migrations.AlterModelOptions(
            name='well',
            options={'verbose_name': 'Скважина', 'verbose_name_plural': 'Скважины'},
        ),
        migrations.RenameField(
            model_name='intersection',
            old_name='layer_id',
            new_name='layer',
        ),
        migrations.RenameField(
            model_name='intersection',
            old_name='well_id',
            new_name='well',
        ),
        migrations.RenameField(
            model_name='layer',
            old_name='asset_id',
            new_name='asset',
        ),
        migrations.RenameField(
            model_name='well',
            old_name='asset_id',
            new_name='asset',
        ),
    ]