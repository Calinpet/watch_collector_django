from django.shortcuts import render, redirect
# Add the following import
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Watch, Strap
# import the ServiceForm
from .forms import ServiceForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def watches_index(request):
  watches = Watch.objects.all()
  return render(request, 'watches/index.html', { 'watches': watches })

# update this view function
def watches_detail(request, watch_id):
  watch = Watch.objects.get(id=watch_id)
  # instantiate FeedingForm to be rendered in the template
  service_form = ServiceForm()

# displaying unassociated straps
  straps_watch_doesnt_have = Strap.objects.exclude(id__in = watch.straps.all().values_list('id'))

  return render(request, 'watches/detail.html', {
    # include the cat and feeding_form in the context
    'watch': watch,
    'service_form': service_form,
    'straps' : straps_watch_doesnt_have,
  })

def add_service(request, watch_id):
  # create the ModelForm using the data in request.POST
  form = ServiceForm(request.POST)
  # validate the form
  if form.is_valid():
    new_service = form.save(commit=False)
    new_service.watch_id = watch_id
    new_service.save()
  return redirect('detail', watch_id=watch_id) 

def assoc_strap(request, watch_id, strap_id,):
  # Note that you can pass a straps id instead of the whole object  
  Watch.objects.get(id=watch_id).straps.add(strap_id)
  return redirect('detail', watch_id=watch_id) 

class WatchCreate(CreateView):
  model = Watch
  fields = ['make', 'model', 'movement', 'description', 'price']
  success_url = '/watches/'

class WatchUpdate(UpdateView):
  model = Watch 
  # Let's disallow the renaming of a watch by excluding the name field!
  fields = ['model', 'movement', 'description', 'price']

class WatchDelete(DeleteView):
  model = Watch
  success_url = '/watches/'

class StrapCreate(CreateView):
  model = Strap
  fields = ('material', 'color')

class StrapUpdate(UpdateView):
  model = Strap
  fields = ('name', 'color')

class StrapDelete(DeleteView):
  model = Strap
  success_url = '/straps/'  

class StrapDetail(DetailView):
  model = Strap
  template_name = 'straps/detail.html'

class StrapList(ListView):
  model = Strap
  template_name = 'straps/index.html'     



