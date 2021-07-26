from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission
from django.core.management import call_command

from library import models
import itertools


class CommandTest(TestCase):

    def setUp(self):
        User.objects.create_user('test_user1', password='4133')
        User.objects.create_user('test_user2', password='4133')

    def test_librarian_create(self):
        args = [user.username for user in User.objects.all()]
        opts = {}
        call_command('create_librarian', *args, **opts)

        group = Group.objects.get(name='librarian')
        users = group.user_set.all()

        self.assertEqual(User.objects.get(id=1).username, users[0].username)
        self.assertEqual(User.objects.get(id=2).username, users[1].username)