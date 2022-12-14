# Generated by Django 4.0.4 on 2022-09-20 08:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caspermun', '0039_about_contacts_main_delete_indexpage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caspermun.artist', verbose_name='Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 14, 15, 1, 674391), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(blank=True, help_text='Track', max_length=1000, null=True, upload_to='tracks/<django.db.models.query_utils.DeferredAttribute object at 0x7f526a74b6d0>/<django.db.models.fields.CharField>', verbose_name='Audio'),
        ),
    ]
