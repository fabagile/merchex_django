# Generated by Django 4.0.2 on 2023-02-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_description_listing_sold_listing_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], max_length=5),
        ),
    ]
