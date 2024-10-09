from django.db import models

# Create your models here.
class movies(models.Model):
  movien=models.CharField(max_length=30)
  heroinen=models.CharField(max_length=30)
  heron=models.CharField(max_length=30)

  def __str__(self):
    return self.movien

