from django.db import models


# Create your models here.
class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name
