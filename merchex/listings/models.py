from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP: 'HH'
        SYNTH_POP: 'SP'
        ALTERNATIVE_ROCK: 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):
    class ListingType(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'

    title = models.fields.CharField(max_length=100, default='')
    description = models.fields.CharField(max_length=1000, default='')
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(blank=True, null=True)
    type = models.fields.CharField(choices=ListingType.choices, max_length=5)
