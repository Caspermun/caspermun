# Generated by Django 4.0.4 on 2022-09-13 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspermun', '0005_alter_album_options_remove_album_upload_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-upload_date'], 'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AddField(
            model_name='album',
            name='upload_date',
            field=models.DateTimeField(default=datetime.date(2022, 9, 13), verbose_name='Upload date'),
        ),
    ]
