from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Assign roles to users'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user')
        parser.add_argument('role', type=str, choices=['User', 'Admin'], help='Role to assign')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        role = kwargs['role']

        user = User.objects.get(username=username)
        group = Group.objects.get(name=role)
        user.groups.add(group)

        self.stdout.write(self.style.SUCCESS(f'Role {role} assigned to user {username}'))