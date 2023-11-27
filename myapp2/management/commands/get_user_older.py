from django.core.management.base import BaseCommand
from myapp2.models import User, Product, Order


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('old', type=int, help='User хрень всякаяid')


    def handle(self, *args, **kwargs):
        res = kwargs['old']
        user = User.objects.filter(age__gt=res)
        self.stdout.write(f'{user}')
