from django.shortcuts import render
# Add the following import
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

def watches_detail(request, watch_id):
  watch = Watch.objects.get(id=watch_id)
  return render(request, 'watches/detail.html', { 'watch': watch })

