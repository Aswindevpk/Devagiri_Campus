# Generated by Django 4.1.7 on 2023-06-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_blooddonation_name_alter_blooddonation_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonatedstudents',
            name='blood_type',
            field=models.CharField(max_length=3),
        ),
    ]
