from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def watches_index(request):
  return render(request, 'watches/index.html', { 'watches': watches })  

class Watch:
  def __init__(self, make, model, movement, description, price):
    self.make = make
    self.model = model
    self.mechanism = movement
    self.description = description
    self.price = price

watches = [
  Watch('TAG Heuer', 'Calibre 16', 'Automatic Chronograph', 'Great watch', 5400),
  Watch('TAG Heur', 'Formula 1', 'Quartz Chronograf', 'Silver grey, fixed ceramic bezel', 2450),
  Watch('G-shock', 'Adventure', 'Quartz', 'Good reliable watch for outdoors', 150)
]    