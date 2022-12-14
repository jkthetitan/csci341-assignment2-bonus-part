# Generated by Django 4.0.6 on 2022-11-20 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.country')),
            ],
        ),
    ]
