from django import forms
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event
# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

class CurrencyInput(forms.NumberInput):
  input_type = 'text'

class AddressInput(forms.TextInput):
  input_type = 'text'


def about(request):
  return render(request, 'about.html')

@login_required
def event_index(request): 
  events = Event.objects.filter(user=request.user)
  return render(request, 'events/index.html', {'events': events})

@login_required
def event_detail(request, event_id):
  event = Event.objects.get(id=event_id)
  return render(request, 'events/detail.html', {'event': event})

class EventCreate(LoginRequiredMixin, CreateView):
  model = Event
  fields = ['name', 'date', 'time', 'category', 'venue', 'address', 'cost', 'celebration', 'description']
  success_url = '/events/'

  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
    form.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})
    form.fields['cost'].widget = CurrencyInput(attrs={'placeholder': '$'})
    form.fields['address'].widget = AddressInput(attrs={"placeholder": '123 Main St, City, State, ZIP, Country'})
    return form
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class EventUpdate(LoginRequiredMixin, UpdateView):
  model = Event
  fields = ['name', 'date', 'time', 'category', 'venue', 'address', 'cost', 'celebration', 'description']

  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
    form.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})
    form.fields['cost'].widget = CurrencyInput(attrs={'placeholder': '$'})
    form.fields['address'].widget = AddressInput(attrs={"placeholder": '123 Main St, City, State, ZIP, Country'})
    return form
  
class EventDelete(LoginRequiredMixin, DeleteView):
  model = Event
  success_url = '/events/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('event-index')
    else:
      error_message= 'Invalid signup - try again'
  form = UserCreationForm()
  context = {'form':form, 'error_message': error_message}
  return render(request, 'signup.html', context)