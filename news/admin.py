from django.contrib import admin
from .models import NewsModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date')
    list_filter = ('title', 'publish_date')
    save_on_top = True
