# Generated by Django 5.0.3 on 2024-03-19 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approved_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.TextField()),
                ('week', models.CharField(max_length=30)),
                ('week_day', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(null=True)),
                ('approved', models.BooleanField(choices=[(True, 'Approved'), (False, 'Not Approved')], default=True)),
                ('feedback', models.TextField()),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supervisor.supervisor')),
            ],
        ),
    ]
