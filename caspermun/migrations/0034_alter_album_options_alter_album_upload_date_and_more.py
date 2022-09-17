# Generated by Django 4.0.4 on 2022-09-17 23:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspermun', '0033_alter_album_options_alter_album_upload_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-id'], 'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AlterField(
            model_name='album',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 5, 37, 57, 857382), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(blank=True, help_text='Track', max_length=1000, null=True, upload_to='tracks/<django.db.models.query_utils.DeferredAttribute object at 0x7f5740352fe0>/<django.db.models.fields.CharField>', verbose_name='Audio'),
        ),
    ]