# Generated by Django 4.0.4 on 2022-09-13 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspermun', '0010_album_status_alter_album_upload_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='status',
        ),
        migrations.AddField(
            model_name='album',
            name='center',
            field=models.BooleanField(blank=True, null=True, verbose_name='Center'),
        ),
        migrations.AddField(
            model_name='album',
            name='left',
            field=models.BooleanField(blank=True, null=True, verbose_name='Left'),
        ),
        migrations.AddField(
            model_name='album',
            name='right',
            field=models.BooleanField(blank=True, null=True, verbose_name='Right'),
        ),
        migrations.AlterField(
            model_name='album',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 15, 53, 39, 627121), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(blank=True, help_text='Track', max_length=1000, null=True, upload_to='tracks/<django.db.models.query_utils.DeferredAttribute object at 0x7ff4d5936560>/<django.db.models.fields.CharField>', verbose_name='Audio'),
        ),
    ]
