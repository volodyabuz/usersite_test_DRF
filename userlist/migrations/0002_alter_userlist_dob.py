# Generated by Django 4.2.7 on 2023-11-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='dob',
            field=models.DateField(blank=True),
        ),
    ]