from http import HTTPStatus

from django.test import Client, TestCase

import parameterized

class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


