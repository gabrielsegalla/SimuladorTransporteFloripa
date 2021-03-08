from django.db import models

class District(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District)

    def __str__(self):
        return self.name