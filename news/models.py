from django.db import models
from rest_framework.reverse import reverse


class NewsModel(models.Model):
    title = models.CharField("Название", max_length=200)
    content = models.TextField("Контент")
    publish_date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "news"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class MenuItem(models.Model):
    title = models.CharField("Название", max_length=50)
    slug = models.SlugField("Урл", max_length=50, blank=True)

    class Meta:
        db_table = "menu_items"
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
    