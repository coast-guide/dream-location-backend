# Generated by Django 4.0.5 on 2022-06-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_municipality_listings_city_listings_picture1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listings',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listings',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listings',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]