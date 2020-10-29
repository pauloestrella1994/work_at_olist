from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=36, null=False)
    edition = models.IntegerField(default=1)
    publication_year = models.DateField()
