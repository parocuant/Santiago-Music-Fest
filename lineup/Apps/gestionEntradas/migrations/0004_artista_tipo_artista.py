# Generated by Django 2.2.7 on 2019-12-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionEntradas', '0003_auto_20191205_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='tipo_Artista',
            field=models.CharField(choices=[('H', 'Headliner'), ('S', 'Support'), ('L', 'Local')], default='?', max_length=1),
        ),
    ]
