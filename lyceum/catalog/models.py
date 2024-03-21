from django.core.exceptions import ValidationError
import django.db


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
    text = django.db.models.TextField(
        "текст",
        validators=[perfect_validator]
    )


class Tag(django.db.models.Model):
     name = django.db.models.CharField(
        "название",
         max_length=150,
     )
     is_published = django.db.models.BooleanField(
         "опубликовано",
         default=True,
     )

    slug = django.db.models.SlugField(
        "слаг"
        max_length=200,
        unique=True,
    )

class Category(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        "опубликовано",
        default=True,
    )
    name = django.db.models.CharField(
        "название",
        max_length=150,
    )
    slug = django.db.models.SlugField(
        "Слаг",
    max_length = 200,
        unique = True,
    )
    weight = django.db.models.IntegerFiled(
        'Вес'
        default = 100,
        null = True,
        blank = True,
    )
