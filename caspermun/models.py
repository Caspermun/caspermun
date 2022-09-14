import datetime

from birthday import BirthdayField
from django.db import models


class IndexPage(models.Model):
    class Meta:
        verbose_name = 'Index page'
        verbose_name_plural = 'Index page'

    logo = models.FileField('Logo', upload_to='logo', help_text='Logo', null=True, blank=True)

    ib_title = models.CharField('Title', max_length=64, null=True, blank=True, help_text='Name')
    ib_image = models.ImageField('Image', upload_to='intro_banner', help_text='Photo')

    ab_title = models.CharField('Title', max_length=512, null=True, blank=True, help_text='About')
    ab_description = models.CharField('Description', max_length=512, null=True, blank=True, help_text='About')

    c_banner = models.ImageField('Banner', upload_to='contact_banner', help_text='Photo', null=True, blank=True)
    c_email = models.URLField('Email', max_length=64, null=True, blank=True)
    c_insta = models.URLField('Instagram', max_length=64, null=True, blank=True)
    c_telegram = models.URLField('Telegram', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.ib_title


class Artist(models.Model):
    nickname = models.CharField('Nickname', max_length=64)
    name = models.CharField('Name', max_length=64)
    surname = models.CharField('Surname', max_length=64)
    image = models.ImageField('Image', upload_to=f'artists/{nickname}', help_text='Photo')
    bio = models.CharField('Bio', max_length=256, null=True, blank=True)
    birthday = BirthdayField('Birthday')

    def __str__(self):
        return self.nickname


class Album(models.Model):
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ['-upload_date']

    title = models.CharField('Title', max_length=64)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Artist')
    cover = models.ImageField('Cover', upload_to=f'tracks/{title}', help_text='Songs cover')
    url = models.CharField('Url', max_length=64, help_text='Url title', null=True, blank=True)
    upload_date = models.DateTimeField('Upload date', default=datetime.datetime.today())

    def __str__(self):
        return f'{self.artist.nickname} - {self.title}'


class Track(models.Model):
    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

    title = models.CharField('Title', max_length=64)
    audio = models.FileField('Audio', upload_to=f'tracks/{Album.title}/{title}', help_text='Track', null=True,
                             blank=True, max_length=1000)
    lyrics = models.TextField('Lyrics', null=True, blank=True, help_text='Song lyrics')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Album')
    artist = models.ManyToManyField(Artist, verbose_name='Artist', related_name='Artist')
    sound_producer = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Sound producer')

    def __str__(self):
        artists = []
        for a in self.artist.all():
            artists.append(a.nickname)
        return f'{",".join(artists)} - {self.title}'


class Link(models.Model):
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    title = models.CharField('Title', max_length=64)
    url = models.URLField('Url', help_text='Url')
    logo = models.FileField('Logo', upload_to='url_logos', help_text='Logo')
    album = models.ForeignKey(Album, verbose_name='Album', on_delete=models.CASCADE, help_text='Album', null=True, blank=True)

    def __str__(self):
        return self.title
