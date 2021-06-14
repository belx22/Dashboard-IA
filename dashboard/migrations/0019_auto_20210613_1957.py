# Generated by Django 3.1.3 on 2021-06-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20210613_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil_sante',
            old_name='blood',
            new_name='Blood',
        ),
        migrations.RenameField(
            model_name='profil_sante',
            old_name='cholesterol',
            new_name='Cholesterol',
        ),
        migrations.RenameField(
            model_name='profil_sante',
            old_name='glucose',
            new_name='Glucose',
        ),
        migrations.RenameField(
            model_name='profil_sante',
            old_name='heart',
            new_name='Heart',
        ),
        migrations.AddField(
            model_name='profil_sante',
            name='Allergies',
            field=models.CharField(default='sugar', max_length=200),
        ),
        migrations.AddField(
            model_name='profil_sante',
            name='BloodType',
            field=models.CharField(default='A+', max_length=200),
        ),
        migrations.AddField(
            model_name='profil_sante',
            name='Diseases',
            field=models.CharField(default='Diabetis', max_length=200),
        ),
    ]
