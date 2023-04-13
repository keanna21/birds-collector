from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Bird
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from django.shortcuts import render, redirect


def add_feeding(request, bird_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
     new_feeding = form.save(commit=False)
     new_feeding.bird_id = bird_id
     new_feeding.save()
  return redirect('detail', bird_id=bird_id)


# Create your views here.
from django.http import HttpResponse

class BirdUpdate(UpdateView):
  model = Bird
  fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/'




class BirdCreate(CreateView):
  model = Bird
  fields = '__all__'
  
  

def home(request):
    return HttpResponse('<h1>Hello World!</h1>')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
     
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    feeding_form = FeedingForm()
    return render(request, 'birds/detail.html', {
       'bird': bird, 'feeding_form': feeding_form
    })