from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello World!</h1>')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
     
    return render(request, 'birds/index.html', {'birds': birds})


class Bird:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

birds = [
  Bird('Screech', 'cardinal', 'red in color', 7),
  Bird('Zippy', 'hummingbird', 'long narrow bill', 0),
  Bird('Scruffy', 'Owl', 'night watcher', 3)
]
