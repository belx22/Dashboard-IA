# Generated by Django 3.1.3 on 2021-06-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210609_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='nationalite',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='photo',
            field=models.CharField(default='', max_length=50),
        ),
    ]