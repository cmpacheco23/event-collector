from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
# from datetime import date

# Create your models here.
CATEGORIES = (
  ('AR', 'Art'),
  ('CH', 'Charity'),
  ('CM', 'Comedy Show'),
  ('CN', 'Conference'),
  ('CO', 'Concert'),
  ('CS', 'Class / Seminar'),
  ('EX', 'Exercise / Fitness'),
  ('FA', 'Fashion'),
  ('FE', 'Festival'),
  ('FI', 'Film'),
  ('FO', 'Food'),
  ('GA', 'Gala'),
  ('MU', 'Music'),
  ('NE', 'Networking'),
  ('OT', 'Other'),
  ('PA', 'Party'),
  ('SP', 'Sports'),
  ('TH', 'Theater'),
  ('WE', 'Wedding'),
  ('WR', 'Work Outing'),
)

CELEBRATION =(
  ('N', 'No'),
  ('Y', 'Yes'),
)

class Event(models.Model):
  name = models.CharField(max_length=150)
  date = models.DateField('Date', default=datetime.date.today)
  time = models.TimeField('Time', default=datetime.time(12, 0))
  category = models.CharField(max_length=2, choices=CATEGORIES, default=[0][0])
  venue = models.CharField(max_length=150)
  address = models.TextField(max_length=250)
  cost = models.IntegerField()
  celebration = models.CharField(max_length=1, choices=CELEBRATION, default=[0][0])
  description = models.TextField(max_length=250)

  def __str__(self):
    return f"{self.get_category_display()} on {self.name}"
  
  def get_absolute_url(self):
    return reverse("event-detail", kwargs={"event_id": self.id})
  
  def event_passed(self):
    return self.date < timezone.now().date()

  class Meta:
    ordering = ['-date']