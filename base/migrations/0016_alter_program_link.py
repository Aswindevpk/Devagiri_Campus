# Generated by Django 4.1.7 on 2023-06-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_program_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]