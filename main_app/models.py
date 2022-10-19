from django.db import models
# Import the reverse function
from django.urls import reverse


# Create your models here.
class Watch(models.Model):
  make = models.CharField(max_length=100) 
  model = models.CharField(max_length=100)
  movement = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  price = models.IntegerField()

  def __str__(self):
      return self.make

# Add this method
  def get_absolute_url(self):
     return reverse('detail', kwargs={'watch_id': self.id})