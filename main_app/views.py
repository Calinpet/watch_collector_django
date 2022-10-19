from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  # instantiate FeedingForm to be rendered in the template
  service_form = ServiceForm()
  return render(request, 'watches/detail.html', { 'watch': watch, 'service_form': service_form })

class WatchCreate(CreateView):
  model = Watch
  fields = '__all__'
  success_url = '/watches/'

class WatchUpdate(UpdateView):
  model = Watch 
  # Let's disallow the renaming of a watch by excluding the name field!
  fields = ['make', 'model', 'movement', 'description', 'price']

class WatchDelete(DeleteView):
  model = Watch
  success_url = '/watches/'



