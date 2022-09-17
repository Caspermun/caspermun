# Generated by Django 4.0.4 on 2022-09-16 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspermun', '0026_alter_album_upload_date_alter_track_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='bg_image',
            field=models.ImageField(blank=True, null=True, upload_to='index', verbose_name='Background image'),
        ),
        migrations.AlterField(
            model_name='album',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 14, 58, 30, 877217), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(blank=True, help_text='Track', max_length=1000, null=True, upload_to='tracks/<django.db.models.query_utils.DeferredAttribute object at 0x7ff983152dd0>/<django.db.models.fields.CharField>', verbose_name='Audio'),
        ),
    ]