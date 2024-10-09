from django.db import models

# Create your models here.

class tweet(models.Model):
  username=models.CharField(max_length=50)
  date=models.DateTimeField(auto_now_add=True)
  post=models.TextField(max_length=100)
  caption=models.CharField(max_length=50)


  def __str__(self):
    return self.username

