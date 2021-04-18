from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(
                email='admin@gmail.com',
                password='admin',
                username='admin'
            )
        except Exception as e:
            print(str(e))