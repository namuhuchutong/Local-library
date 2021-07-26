from django.core.management import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User


MODELS = ['author', 'book', 'genre', 'language', 'book instance']
PERMISSIONS = ['view', 'change', 'delete', 'add']

class Command(BaseCommand):
    help = "Add librarians"

    def add_arguments(self, parser):
        parser.add_argument('librarians', nargs='+', type=str)
    
    def handle(self, *args, **options):
        group, _ = Group.objects.get_or_create(name='librarian')
        perms = []

        for librarian in options['librarians']:
            try:
                target = User.objects.get(username=librarian)
            except User.DoesNotExist:
                raise CommandError("User %s does not exist " % librarian)

            for model in MODELS:
                for permission in PERMISSIONS:
                    name = "Can {} {}".format(permission, model)
                    self.stdout.write("Create {}\n".format(name))
                
                    try:
                        target_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        raise CommandError("Permission : {} does not exist".format(name))
                    
                    perms.append(target_add_perm)

            group.permissions.set(perms)        
            target.groups.add(group)
