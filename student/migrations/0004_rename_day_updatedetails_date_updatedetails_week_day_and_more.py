# Generated by Django 5.0.3 on 2024-03-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_updatedetails_week'),
    ]

    operations = [
        migrations.RenameField(
            model_name='updatedetails',
            old_name='Day',
            new_name='Date',
        ),
        migrations.AddField(
            model_name='updatedetails',
            name='week_day',
            field=models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday')], default='Monday', max_length=30),
        ),
        migrations.AlterField(
            model_name='updatedetails',
            name='week',
            field=models.CharField(choices=[('Week1', 'Week1'), ('Week2', 'Week2'), ('Week3', 'Week3'), ('Week4', 'Week4'), ('Week5', 'Week5'), ('Week6', 'Week6'), ('Week7', 'Week7'), ('Week8', 'Week8'), ('Week9', 'Week9'), ('Week10', 'Week10')], max_length=50),
        ),
    ]
