from http import HTTPStatus

import catalog.models
from django.core.exceptions import ValidationError
from django.test import Client, TestCase
import parameterized


class StaticURlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)


class StaticURL(TestCase):
    @parameterized.parameterized.expand(
        [
            ("0", HTTPStatus.OK),
            ("1", HTTPStatus.OK),
            ("01", HTTPStatus.OK),
            ("010", HTTPStatus.OK),
            ("10", HTTPStatus.OK),
            ("100", HTTPStatus.OK),
            ("abcd", HTTPStatus.NOT_FOUND),
            ("aa4a", HTTPStatus.NOT_FOUND),
            ("232%", HTTPStatus.NOT_FOUND),
            ("-0", HTTPStatus.NOT_FOUND),
            ("-1", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_kik(self, kik, expected_status):
        status_code = Client().get(f"/catalog/{kik}/").status_code
        self.assertEqual(
            status_code,
            expected_status,
            msg=f"/catalog/{kik}/ get not {expected_status}",
        )


class StaticURLTest(TestCase):
    @parameterized.parameterized.expand(
        [
            ("0", HTTPStatus.NOT_FOUND),
            ("1", HTTPStatus.OK),
            ("01", HTTPStatus.NOT_FOUND),
            ("010", HTTPStatus.NOT_FOUND),
            ("10", HTTPStatus.OK),
            ("100", HTTPStatus.OK),
            ("abcd", HTTPStatus.NOT_FOUND),
            ("aa4a", HTTPStatus.NOT_FOUND),
            ("232%", HTTPStatus.NOT_FOUND),
            ("-0", HTTPStatus.NOT_FOUND),
            ("-1", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_kio(self, kio, expected_status):
        status_code = Client().get(f"/catalog/re/{kio}/").status_code
        self.assertEqual(
            status_code,
            expected_status,
            msg=f"/catalog/re/{kio}/ get not {expected_status}",
        )


class StaticUrlTest(TestCase):
    @parameterized.parameterized.expand(
        [
            ("0", HTTPStatus.NOT_FOUND),
            ("1", HTTPStatus.OK),
            ("01", HTTPStatus.NOT_FOUND),
            ("010", HTTPStatus.NOT_FOUND),
            ("10", HTTPStatus.OK),
            ("100", HTTPStatus.OK),
            ("abcd", HTTPStatus.NOT_FOUND),
            ("aa4a", HTTPStatus.NOT_FOUND),
            ("232%", HTTPStatus.NOT_FOUND),
            ("-0", HTTPStatus.NOT_FOUND),
            ("-1", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_kill(self, kill, expected_status):
        status_code = Client().get(f"/catalog/converter/{kill}/").status_code

        self.assertEqual(
            status_code,
            expected_status,
            msg=f"/catalog/converter/{kill}/ get not {expected_status}",
        )


class DBItemTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = catalog.models.Category.objects.create(
            name="Test Category",
        )
        cls.tag = catalog.models.Tag.objects.create(
            name="Test Tag",
        )

    @parameterized.parameterized.expand(
        [
            ("test", "превосходно", True),
            ("test", "роскошно", True),
            ("test", "Я превосходно", True),
            ("test", "превосходно Я", True),
            ("test", "превосходно роскошно", True),
            ("test", "роскошно!", True),
            ("test", "!роскошно", True),
            ("test", "!роскошно", True),
            ("test", "роскошно©", True),
            ("test", "превосходноН", False),
            ("test", "превНосходно", False),
            ("test", "Нпревосходно", False),
            ("test", "Я превосх%одно", False),
            ("test", "превосходнороскошно", False),
            ("test" * 38, "превосходно", False),
        ],
    )
    def test_add_item(self, name, text, is_validate):
        item_count = catalog.models.Item.objects.count()
        item = catalog.models.Item(
            name=name,
            text=text,
            category=self.category,
        )
        if not is_validate:
            with self.assertRaises(ValidationError):
                item.full_clean()
                item.save()
                item.tags.add(self.tag)
                item.full_clean()
                item.save()

            self.assertEqual(
                catalog.models.Item.objects.count(),
                item_count,
                msg="add no validate item",
            )
        else:
            item.full_clean()
            item.save()
            item.tags.add(self.tag)
            self.assertEqual(
                catalog.models.Item.objects.count(),
                item_count + 1,
                msg="no add validate item",
            )

    def test_add_category(self):
        category_count = catalog.models.Category.objects.count()
        new_category = catalog.models.Category(name="New Test Category")
        new_category.full_clean()
        new_category.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            category_count + 1,
            msg="category not added",
        )

    def test_add_tag(self):
        tag_count = catalog.models.Tag.objects.count()
        new_tag = catalog.models.Tag(name="New Test Tag")
        new_tag.full_clean()
        new_tag.save()
        self.assertEqual(
            catalog.models.Tag.objects.count(),
            tag_count + 1,
            msg="tag not added",
        )
