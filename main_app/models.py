from django.db import models
from django.urls import reverse



# Create your models here.
class Bird(models.Model):
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()
	def get_absolute_url(self):
		return reverse('detail', kwargs={'bird_id': self.id})
	
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
	
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
	 choices=MEALS,
	 default=MEALS[0][0]
  )
  
  class Meta:
    ordering = ['-date']

  bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
