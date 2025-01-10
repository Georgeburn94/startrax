from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User  # Import Django's built-in User model
from datetime import date

class Album(models.Model):
    id = models.AutoField(primary_key=True)  # Primary Key
    name = models.CharField(max_length=255)  # Name of the album
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(date.today().year)]  # Ensure year is not in the future
    )
    artist = models.CharField(max_length=100)  # Name of the artist

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")  # FK to User
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="reviews")  # FK to Album
    star_rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # Rating between 1 and 5
    )
    note = models.TextField(blank=True, null=True)  # Optional note