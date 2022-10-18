from django.shortcuts import render
# Add the following import
from django.http import HttpResponse
from .models import Watch

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def watches_index(request):
  watches = Watch.objects.all()
  return render(request, 'watches/index.html', { 'watches': watches })  

watches = [
  Watch('TAG Heuer', 'Calibre 16', 'Automatic Chronograph', 'Great watch', 5400),
  Watch('TAG Heur', 'Formula 1', 'Quartz Chronograf', 'Silver grey, fixed ceramic bezel', 2450),
  Watch('G-shock', 'Adventure', 'Quartz', 'Good reliable watch for outdoors', 150)
]   