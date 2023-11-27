from django.core.management.base import BaseCommand
from myapp2.models import User, Product, Order, Author

from myapp2.models import Atest


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com',
        #             password='secret', age=25)
        # user = User(name='Neo', email='neo@example.com', password='secret',
        #             age=58)
        author = Atest(name='1Name', email='111mail@mail.ru')
        author.save()
        self.stdout.write(f'choto cdelali {author}')
