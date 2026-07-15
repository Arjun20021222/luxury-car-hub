from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


class Command(BaseCommand):
    help = "Creates a superuser if one doesn't already exist."

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = "admin"
        email = "admin@example.com"
        password = "Admin@12345"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            self.stdout.write(
                self.style.SUCCESS("Superuser created successfully.")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Superuser already exists.")
            )