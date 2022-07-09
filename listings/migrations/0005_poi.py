# Generated by Django 4.0.5 on 2022-07-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_remove_listings_location_listings_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('type', models.CharField(choices=[('University', 'University'), ('Hospital', 'Hospital'), ('Stadium', 'Stadium')], max_length=50)),
            ],
        ),
    ]
