from django.db import models


# Create your models here.
class Pokemon(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.IntegerField()
    name = models.CharField(max_length=30)
    lvl = models.IntegerField()
    xp = models.IntegerField()
    number = models.IntegerField()
    type_1 = models.CharField(max_length=30)
    type_2 = models.CharField(max_length=30)
    special_capacity = models.CharField(max_length=30)
    memo = models.CharField(max_length=30)
    atck = models.IntegerField(default=0)
    defs = models.IntegerField(default=0)
    atck_spe = models.IntegerField(default=0)
    defs_spe = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    hp = models.IntegerField()
    team_id = models.IntegerField()
    shiny = models.BooleanField(default=False)
    image_url = models.CharField(max_length=100)
    shiny_image_url = models.CharField(max_length=100)


    def __str__(self):
        return "Pokemon: " + self.name + " - " + str(self.lvl) + " - " + str(self.xp) + " - " + str(
            self.number) + " - " + self.type_1 + " - " + self.type_2 + " - " + self.special_capacity + " - " + self.memo + " - " + str(
            self.atck) + " - " + str(self.defs) + " - " + str(self.atck_spe) + " - " + str(self.defs_spe) + " - " + str(
            self.speed) + " - " + str(self.hp) + " - " + str(
            self.team_id) + " - " + self.image_url + " - " + self.shiny_image_url + " - " + str(self.shiny)
