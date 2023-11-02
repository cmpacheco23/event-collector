from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Event
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def event_index(request): 
  events = Event.objects.all()
  return render(request, 'events/index.html', {'events': events})

def event_detail(request, event_id):
  event = Event.objects.get(id=event_id)
  return render(request, 'events/detail.html', {'event': event})

class EventCreate(CreateView):
  model = Event
  fields = '__all__'
  success_url = '/events/'