# Generated by Django 3.1.3 on 2021-06-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('email', models.EmailField(blank='true', max_length=254, unique=True)),
                ('PwdAdministrateur', models.CharField(blank='true', max_length=15)),
                ('PhotoAdministrateur', models.ImageField(default='image.png', upload_to='')),
                ('actif', models.CharField(default='oui', max_length=3)),
            ],
        ),
    ]