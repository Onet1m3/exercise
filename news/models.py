from django.db import models


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
