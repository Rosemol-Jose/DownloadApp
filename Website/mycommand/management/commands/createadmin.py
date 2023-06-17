from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create an admin user'

    def handle(self, *args, **options):
        username = input("Enter your username")
        email = input("Enter your email")
        password = input("Enter Password")

        # Create the admin user
        User.objects.create_superuser(username, email, password)

        self.stdout.write(self.style.SUCCESS('Admin user created successfully.'))
