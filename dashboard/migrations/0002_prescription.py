# Generated by Django 3.2.4 on 2021-06-06 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medication', models.CharField(max_length=50)),
                ('Notes', models.TextField(max_length=50)),
                ('date', models.DateTimeField()),
                ('NomDocteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.docteur')),
                ('NomPatient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patient')),
            ],
        ),
    ]
