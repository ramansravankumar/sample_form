# Generated by Django 5.0.1 on 2024-03-15 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_person_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
