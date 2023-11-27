from django.core.management.base import BaseCommand
from myapp2.models import User, Product, Order


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        user = User.objects.filter(id=id).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')
