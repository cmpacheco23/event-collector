from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Event
# Create your views here.

class CurrencyInput(forms.NumberInput):
  input_type = 'text'

class AddressInput(forms.TextInput):
  input_type = 'text'

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

  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
    form.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})
    form.fields['cost'].widget = CurrencyInput(attrs={'placeholder': '$'})
    form.fields['address'].widget = AddressInput(attrs={"placeholder": '123 Main St, City, State, ZIP, Country'})

    return form
  
class EventUpdate(UpdateView):
  model = Event
  fields = ['name', 'date', 'time', 'category', 'venue', 'address', 'cost', 'celebration', 'description'] 

  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
    form.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})
    form.fields['cost'].widget = CurrencyInput(attrs={'placeholder': '$'})
    form.fields['address'].widget = AddressInput(attrs={"placeholder": '123 Main St, City, State, ZIP,'})


class EventDelete(DeleteView):
  model = Event
  success_url = '/events/'
