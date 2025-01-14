# Generated by Django 4.1.5 on 2023-10-11 00:52

from django.db import migrations, models
import geodesk_gis.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_filename', models.CharField(blank=True, max_length=128, null=True)),
                ('file', models.FileField(blank=True, max_length=1000, null=True, upload_to=geodesk_gis.models.get_map_file_uploader_path)),
            ],
        ),
        migrations.CreateModel(
            name='MapFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_row', models.IntegerField(default=None, null=True)),
                ('expected_filename', models.CharField(blank=True, max_length=128, null=True)),
                ('file', models.FileField(blank=True, max_length=1000, null=True, upload_to=geodesk_gis.models.get_map_file_uploader_path)),
            ],
        ),
    ]
