# Generated by Django 4.0.6 on 2022-11-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseType',
            fields=[
                ('dt_id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=140)),
            ],
        ),
    ]