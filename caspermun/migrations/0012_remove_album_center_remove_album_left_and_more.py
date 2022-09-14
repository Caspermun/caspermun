# Generated by Django 4.0.4 on 2022-09-13 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspermun', '0011_remove_album_status_album_center_album_left_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='center',
        ),
        migrations.RemoveField(
            model_name='album',
            name='left',
        ),
        migrations.RemoveField(
            model_name='album',
            name='right',
        ),
        migrations.AlterField(
            model_name='album',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 16, 20, 12, 497185), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(blank=True, help_text='Track', max_length=1000, null=True, upload_to='tracks/<django.db.models.query_utils.DeferredAttribute object at 0x7f1cf4f4a500>/<django.db.models.fields.CharField>', verbose_name='Audio'),
        ),
    ]
