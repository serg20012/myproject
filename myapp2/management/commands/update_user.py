from django.core.management.base import BaseCommand
from myapp2.models import User, Product, Order


class Command(BaseCommand):
    help = "Get user bdssdasdsa id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('new_name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('new_name')
        user = User.objects.filter(pk=pk).first()
        print(user)
        user.name = name
        user.save()
        self.stdout.write(f'{user}')
