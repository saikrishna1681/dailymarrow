from django.db import models
# Create your models here.

POSSIBLE_MOVIE_STATUS = [
    ("Canceled", "Canceled"),
    ("Planned", "Planned"),
    ("In Production", "In Production"),
    ("Post Production", "Post Production"),
    ("Released", "Released"),
    ("Rumored", "Rumored"),
    ("", "")
]

class ProductionCompany(models.Model):
    name = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length= 100)


class Languages(models.Model):
    name = models.CharField(max_length=100)


class Movie_data(models.Model):

    budget = models.FloatField(default = 0)
    homepage = models.URLField(max_length = 1000, blank = True, null = True)
    original_language_code = models.CharField(max_length = 5)
    original_title = models.CharField(max_length = 1000)
    overview = models.TextField(blank=True)
    release_date = models.DateField(null = True)
    revenue = models.FloatField(default = 0)
    runtime = models.FloatField(default = 0)
    status = models.CharField(max_length = 20, choices = POSSIBLE_MOVIE_STATUS, default = "", blank = True)
    title = models.CharField(max_length = 1000)
    rating = models.FloatField(default = 0)
    vote_count = models.IntegerField(default = 0)
    # production_company = models.ForeignKey(ProductionCompany, on_delete= models.CASCADE)
    # genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null = True)
    production_company_id = models.IntegerField(default = 0)
    genre_id = models.IntegerField(default = 0)
    languages = models.TextField()









