from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from startrax.models import Album, Review

class Command(BaseCommand):
    help = 'Create user roles and assign permissions'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Running create_roles command...'))

        # Create groups
        user_group, created = Group.objects.get_or_create(name='User')
        admin_group, created = Group.objects.get_or_create(name='Admin')

        # Assign permissions to admin group
        content_types = [ContentType.objects.get_for_model(Album), ContentType.objects.get_for_model(Review)]
        permissions = Permission.objects.filter(content_type__in=content_types)
        admin_group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS('Roles and permissions created successfully'))