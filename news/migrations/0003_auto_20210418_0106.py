# Generated by Django 3.1.7 on 2021-04-17 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Урл'),
        ),
    ]
