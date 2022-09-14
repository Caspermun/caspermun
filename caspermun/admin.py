from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from caspermun.models import *


class TrackInline(admin.TabularInline):
    model = Track
    insert_after = 'cover'
    extra = 1


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        TrackInline,
        LinkInline,
    ]


class IndexPageAdminForm(forms.ModelForm):
    ab_title = forms.CharField(label='Title', widget=CKEditorUploadingWidget())
    ab_description = forms.CharField(label='Description', widget=CKEditorUploadingWidget())

    class Meta:
        model = IndexPage
        fields = '__all__'


@admin.register(IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    form = IndexPageAdminForm


admin.site.register(Artist)
