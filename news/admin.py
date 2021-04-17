from django.contrib import admin
from .models import NewsModel, MenuItem


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date')
    list_filter = ('title', 'publish_date')
    save_on_top = True

@admin.register(MenuItem)
class MenuItemlAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {"slug": ("title",)}