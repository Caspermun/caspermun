# Generated by Django 4.1.1 on 2022-09-20 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspermun', '0043_alter_album_upload_date_alter_track_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 21, 0, 25, 15, 342499), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(blank=True, help_text='Track', max_length=1000, null=True, upload_to='tracks/<django.db.models.query_utils.DeferredAttribute object at 0x7f19ac15d600>/<django.db.models.fields.CharField>', verbose_name='Audio'),
        ),
    ]
