from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create_user(username='user1', password='password1')
        user2 = User.objects.create_user(username='user2', password='password2')

        # Create tasks
        Task.objects.create(title='Task 1', link='http://example.com/1', status=False)
        Task.objects.create(title='Task 2', link='http://example.com/2', status=True)
        Task.objects.create(title='Task 3', link='http://example.com/3', status=False)
        Task.objects.create(title='Task 4', link='http://example.com/4', status=True)
        Task.objects.create(title='Task 5', link='http://example.com/5', status=True)
        Task.objects.create(title='Task 6', link='http://example.com/6', status=False)
        Task.objects.create(title='Task 7', link='http://example.com/7', status=True)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
