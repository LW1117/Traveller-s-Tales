# Generated by Django 4.2.1 on 2023-06-18 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_location_delete_destination'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['date']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='review',
            order_with_respect_to=None,
        ),
    ]
