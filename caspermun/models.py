import datetime

import mutagen
from birthday import BirthdayField
from django.db import models
from django.utils.html import format_html


class Main(models.Model):
    class Meta:
        verbose_name = 'Main'
        verbose_name_plural = 'Main'

    logo = models.FileField('Logo', upload_to='logo', help_text='Logo', )
    title = models.CharField('Title', max_length=64, help_text='Name')
    image = models.ImageField('Intro image', upload_to='intro_banner', help_text='Photo')
    bg_image = models.ImageField('For mobile devices', upload_to='index', null=True, blank=True)
    views = models.IntegerField(default=0, verbose_name='Views')

    def save(self, *args, **kwargs):
        if Main.objects.count() >= 1:
            return super(Main, self).save(False)
        else:
            return super(Main, self).save(*args, **kwargs)

    def __str__(self):
        return 'Main'


class Artist(models.Model):
    nickname = models.CharField('Nickname', max_length=64)
    name = models.CharField('Name', max_length=64)
    surname = models.CharField('Surname', max_length=64)
    image = models.ImageField('Image', upload_to=f'artists/{nickname}', help_text='Photo', null=True, blank=True)
    bio = models.TextField('Bio', help_text='Shows in about page', default='')
    birthday = BirthdayField('Birthday')

    def __str__(self):
        return self.nickname


class About(models.Model):
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Artist')
    banner = models.ImageField('About image', upload_to='about', null=True, blank=True)

    def save(self, *args, **kwargs):
        if About.objects.count() >= 1:
            return super(About, self).save(False)
        else:
            return super(About, self).save(*args, **kwargs)

    def __str__(self):
        return 'About'


class Contacts(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    banner = models.ImageField('Contact banner', upload_to='contact_banner', help_text='Background image')
    deal = models.EmailField('Deal', max_length=64)
    booking = models.EmailField('Booking', max_length=64)
    insta = models.URLField('Instagram', max_length=64)
    youtube = models.URLField('YouTube', max_length=64)
    tiktok = models.URLField('TikTok', max_length=64)
    telegram = models.URLField('Telegram', max_length=64)

    def save(self, *args, **kwargs):
        if Contacts.objects.count() >= 1:
            return super(Contacts, self).save(False)
        else:
            return super(Contacts, self).save(*args, **kwargs)

    def __str__(self):
        return 'Contacts'


GENRE_CHOICES = (
    ('hh', 'Hip-Hop/Rap'),
    ('trap', 'Trap'),
    ('rb', 'R&B'),
    ('pop', 'Pop'),
)


class Album(models.Model):
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ['-id']

    title = models.CharField('Title', max_length=64)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Artist')
    cover = models.ImageField('Cover', upload_to=f'tracks/{title}', help_text='Songs cover')
    genre = models.CharField('Genre', choices=GENRE_CHOICES, default='hh', max_length=64)
    explicit = models.BooleanField('Explicit', default=False)
    url = models.CharField('Url', max_length=64, help_text='Url title')
    html = models.URLField('Apple Music', help_text='Embed code', default='')
    upload_date = models.DateTimeField('Upload date', default=datetime.datetime.today())
    views = models.IntegerField(default=0, verbose_name='Views')

    def cover_tag(self):
        from django.utils.html import escape
        return format_html('<img src="/media/%s" width="100px" />' % format(self.cover))

    cover_tag.short_description = 'Check cover'
    cover_tag.allow_tags = True


class Track(models.Model):
    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

    title = models.CharField('Title', max_length=64)
    audio = models.FileField('Audio', upload_to=f'tracks/{Album.title}/{title}', help_text='Track', null=True,
                             blank=True, max_length=1000)
    # duration = models.CharField("Track duration", blank=True, null=True, max_length=8)
    lyrics = models.TextField('Lyrics', null=True, blank=True, help_text='Song lyrics')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Album')
    artist = models.ManyToManyField(Artist, verbose_name='Artist', related_name='Artist')
    sound_producer = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Sound producer')
    explicit = models.BooleanField('Explicit', default=False)

    def audio_tag(self):
        return format_html(
            '<audio controls name="media"><source src="/media/%s" type="audio/mpeg"></audio>' % format(self.audio))

    audio_tag.short_description = 'Audio play'
    audio_tag.allow_tags = True

    @property
    def duration(self):
        audio_info = mutagen.File(self.audio).info
        length = int(audio_info.length)
        minutes = length // 60
        return str(minutes) + ':' + str(length - minutes * 60)

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
    album = models.ForeignKey(Album, verbose_name='Album', on_delete=models.CASCADE, help_text='Album')

    def __str__(self):
        return self.title
