from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from caspermun.models import *


class TrackInline(admin.TabularInline):
    model = Track
    extra = 1


class TrackAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('title', 'audio_tag', 'audio', 'lyrics', 'album', 'artist', 'sound_producer')}),)
    readonly_fields = ('audio_tag',)


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        TrackInline,
        LinkInline,
    ]

    fieldsets = ((None, {'fields': ('title', 'artist', 'cover_tag', 'cover', 'url', 'upload_date', 'views')}),)
    readonly_fields = ('cover_tag',)
    list_display = ('artist', 'title', 'cover_tag')
    list_display_links = ('artist', 'title', 'cover_tag')
    search_fields = ('title__icontains', 'artist__nickname__icontains')
    list_per_page = 10


class IndexPageAdminForm(forms.ModelForm):
    class Meta:
        model = IndexPage
        fields = '__all__'

    ab_title = forms.CharField(label='Title', widget=CKEditorUploadingWidget())
    ab_description = forms.CharField(label='Description', widget=CKEditorUploadingWidget())


@admin.register(IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    form = IndexPageAdminForm

    def has_add_permission(self, request, obj=None):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('nickname', 'name', 'surname', 'image', 'bio', 'birthday')}),)
    list_display = ('nickname', 'name', 'surname')
    list_display_links = ('nickname', 'name', 'surname')
