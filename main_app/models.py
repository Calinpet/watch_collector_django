from django.db import models
# Import the reverse function
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# A tuple of 2-tuples
PERIOD = (
  ('A', 'Annualy'),
  ('Q', 'Quartely'),
  ('M', 'Monthly')
)
class Strap(models.Model):
  material = models.CharField(max_length=50)
  color = models.CharField(max_length=50)

  def get_absolute_url(self):
      return reverse('straps_detail', kwargs={'pk': self.id})

# Create your models here.
class Watch(models.Model):
  make = models.CharField(max_length=100) 
  model = models.CharField(max_length=100)
  movement = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  price = models.IntegerField()
  straps = models.ManyToManyField(Strap)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

 # changes to instance methods do not require re-generation / running of migrations
  def __str__(self):
      return self.make

# Add this method
  def get_absolute_url(self):
     return reverse('detail', kwargs={'watch_id': self.id})

class Service(models.Model):
  date = models.DateField('service date')
  period = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=PERIOD,
    # set the default value for meal to be 'B'
    default=PERIOD[0][0]
  ) 

  # Create a watch_id FK
  watch = models.ForeignKey(Watch, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_service_display()} on {self.date}"
  # change the default sort
  class Meta:
    ordering = ['-date']  
