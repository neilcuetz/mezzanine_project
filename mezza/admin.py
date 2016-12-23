from django.contrib import admin

from mezza.models import Banner
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'title',
            'image',
    )
    search_field = (
            'title'
    )


admin.site.register(Banner, BannerAdmin)
