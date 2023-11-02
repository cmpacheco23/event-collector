from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=150)
  date = models.CharField(max_length=50)
  time = models.CharField(max_length=50)
  category = models.CharField(max_length=50)
  venue = models.CharField(max_length=150)
  address = models.TextField(max_length=250)
  cost = models.CharField(max_length=50)
  celebration = models.CharField(max_length=50)
  description = models.TextField(max_length=250)

  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
      return reverse("event-detail", kwargs={"event_id": self.id})
  
