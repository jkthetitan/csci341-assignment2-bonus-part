# Generated by Django 4.0.6 on 2022-11-20 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicServant',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.users')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]