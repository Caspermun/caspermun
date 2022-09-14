# Generated by Django 4.0.4 on 2022-09-13 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspermun', '0008_track_audio_alter_album_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 13, 15, 11, 965569), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(blank=True, help_text='Track', max_length=1000, null=True, upload_to='tracks/<django.db.models.query_utils.DeferredAttribute object at 0x7fd785f4a4d0>/<django.db.models.fields.CharField>', verbose_name='Audio'),
        ),
    ]
