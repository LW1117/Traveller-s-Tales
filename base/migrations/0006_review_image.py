# Generated by Django 4.2.1 on 2023-06-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_review_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='review_images/'),
        ),
    ]
