# Generated by Django 4.0.4 on 2022-09-20 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspermun', '0038_alter_album_upload_date_alter_track_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='about', verbose_name='About image')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(help_text='Background image', upload_to='contact_banner', verbose_name='Contact banner')),
                ('deal', models.EmailField(max_length=64, verbose_name='Deal')),
                ('booking', models.EmailField(max_length=64, verbose_name='Booking')),
                ('insta', models.URLField(max_length=64, verbose_name='Instagram')),
                ('youtube', models.URLField(max_length=64, verbose_name='YouTube')),
                ('tiktok', models.URLField(max_length=64, verbose_name='TikTok')),
                ('telegram', models.URLField(max_length=64, verbose_name='Telegram')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(help_text='Logo', upload_to='logo', verbose_name='Logo')),
                ('title', models.CharField(help_text='Name', max_length=64, verbose_name='Title')),
                ('image', models.ImageField(help_text='Photo', upload_to='intro_banner', verbose_name='Intro image')),
                ('bg_image', models.ImageField(blank=True, null=True, upload_to='index', verbose_name='For mobile devices')),
            ],
            options={
                'verbose_name': 'Main',
                'verbose_name_plural': 'Main',
            },
        ),
        migrations.DeleteModel(
            name='IndexPage',
        ),
        migrations.AlterField(
            model_name='album',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 13, 31, 57, 123708), verbose_name='Upload date'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.CharField(blank=True, help_text='Shows in about page', max_length=256, null=True, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(blank=True, help_text='Track', max_length=1000, null=True, upload_to='tracks/<django.db.models.query_utils.DeferredAttribute object at 0x7f054bd3b400>/<django.db.models.fields.CharField>', verbose_name='Audio'),
        ),
    ]
