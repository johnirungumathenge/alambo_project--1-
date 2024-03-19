# Generated by Django 5.0.3 on 2024-03-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('regno', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('img', models.ImageField(upload_to='supervisor')),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]