# Generated by Django 3.0 on 2020-10-09 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylife', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='ciudad_mia',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='nombre_mio',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_publicacion',
            field=models.DateTimeField(verbose_name='published_date'),
        ),
    ]