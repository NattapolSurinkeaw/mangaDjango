from django.contrib import admin
from manga.models import Category, Cartoon, Episode, ImageCartoon


# Register your models here.
admin.site.register(Category)

admin.site.register(Cartoon)

class EpisodeCartoonAdmin(admin.ModelAdmin):
    list_display = ('get_cartoon_name', 'name_episode')

    def get_cartoon_name(self, obj):
        return obj.cartoon_id.name_cartoon
    get_cartoon_name.short_description = 'Cartoon'

admin.site.register(Episode, EpisodeCartoonAdmin)

class ImageCartoonAdmin(admin.ModelAdmin):
    list_display = ('get_cartoon_name', 'title_image', 'episode_id', 'priority', 'date')

    def get_cartoon_name(self, obj):
        return obj.episode_id.cartoon_id.name_cartoon  # เข้าถึงชื่อการ์ตูนผ่านความสัมพันธ์
    get_cartoon_name.short_description = 'Cartoon'  # กำหนดชื่อคอลัมน์ใน Admin

admin.site.register(ImageCartoon, ImageCartoonAdmin)