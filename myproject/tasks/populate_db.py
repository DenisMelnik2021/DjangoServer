from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Создание пользователей
        user1 = User.objects.create_user(username='user1', password='password1')
        user2 = User.objects.create_user(username='user2', password='password2')

        # Создание задач
        Task.objects.create(title='улица Юности', link='https://yandex.ru/maps/-/CDtlRGkM', status=False)
        Task.objects.create(title='Яблоневая аллея', link='https://yandex.ru/maps/-/CDtlVNig', status=True)
        Task.objects.create(title='3-й микрорайон', link='https://yandex.ru/maps/-/CDtlVCYC', status=False)
        Task.objects.create(title='4-й микрорайон', link='https://yandex.ru/maps/-/CDtlVO9Z', status=True)
        Task.objects.create(title='Зеленоград, к405', link='https://yandex.ru/maps/-/CDtlV8ix', status=True)
        Task.objects.create(title='Берёзовая аллея', link='https://yandex.ru/maps/-/CDtlVPio', status=False)
        Task.objects.create(title='улица Болдов Ручей', link='https://yandex.ru/maps/-/CDtlV22o', status=True)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
