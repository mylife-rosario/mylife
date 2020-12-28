# Generated by Django 3.0 on 2020-11-01 02:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mylife', '0003_auto_20201009_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('comentario_aprovado', models.BooleanField(default=False)),
                ('enviar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mylife.Publicacion')),
            ],
        ),
    ]