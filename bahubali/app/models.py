from django.db import models 

# Create your models here.
class bookitem(models.Model):
  name=models.CharField(max_length=30)
  pages=models.IntegerField()
  price=models.IntegerField()

  def __str__(self):
    return self.name