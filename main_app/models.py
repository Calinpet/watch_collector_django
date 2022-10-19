from django.db import models
# Import the reverse function
from django.urls import reverse

# A tuple of 2-tuples
PERIOD = (
  ('A', 'Annualy'),
  ('Q', 'Quartely'),
  ('M', 'Monthly')
)

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

class Service(models.Model):
  date = models.DateField()
  period = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=PERIOD,
    # set the default value for meal to be 'B'
    default=PERIOD[0][0]
  ) 

  # Create a watch_id FK
  cat = models.ForeignKey(Watch, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_period_display()} on {self.date}"
