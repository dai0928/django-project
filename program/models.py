from django.db import models


class SearchModel(models.Model):
    text = models.CharField(max_length=100)
