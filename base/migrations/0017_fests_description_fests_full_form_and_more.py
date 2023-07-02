# Generated by Django 4.1.7 on 2023-07-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_program_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='fests',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fests',
            name='full_form',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to='media/carousel_images/'),
        ),
        migrations.AlterField(
            model_name='explore',
            name='image',
            field=models.ImageField(upload_to='media/explore_images'),
        ),
        migrations.AlterField(
            model_name='fests',
            name='logo',
            field=models.ImageField(default='default_image.jpg', upload_to='media/fest_logos'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='media/news_images'),
        ),
    ]
