"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from django_dict import models

class SimpleTest(TestCase):

    def test_save_model(self):
        models.Dictionary.objects.create(name = "foo", label = "bar", type="foo")
