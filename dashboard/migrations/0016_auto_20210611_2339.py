# Generated by Django 3.1.3 on 2021-06-11 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_docteur_specialisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docteur',
            name='photo',
            field=models.CharField(default='default.png', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='photo',
            field=models.CharField(default='default.png', max_length=50),
        ),
    ]
