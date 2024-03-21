import django.db

from django.db import models
from django.core.exceptions import ValidationError


def perfect_validator(value):
    if "превосходно" in value.lower().split():
        return
    if "роскошно" in value.lower().split():
        return
    raise ValidationError("нету слово роскошно или превосходно")


class Item(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        "опубликовано",
        default=True,
    )
    name = django.db.models.CharField(
        "название",
        max_length=150,
    )
    text = django.db.models.TextField("текст", validators=[perfect_validator])


class Tag(django.db.models.Model):
    name = django.db.models.CharField("название", max_length=150,)
    Item = models.ManyToManyField(Item),

    is_published = django.db.models.BooleanField(
        "опубликовано",
        default=True,
    )

    slug = django.db.models.SlugField(
        "слаг",
        max_length=200,
        unique=True,
    )


class Category(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        "опубликовано",
        default=True,
    )
    name = django.db.models.CharField("название", max_length=150, )
    Tag = models.ManyToManyField(Tag),
    Item = models.ManyToManyField(Item),

    slug = django.db.models.SlugField(
        "Слаг",
        max_length=200,
        unique=True,
    )
    weight = django.db.models.IntegerField(
        "Вес",
        default=100,
        null=True,
        blank=True,
    )
