from django.core.management.base import BaseCommand
from myapp2.models import User, Product, Order


class Command(BaseCommand):
    help = "Get all user"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')
