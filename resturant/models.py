from django.db import models

# Create your models here.
# Create model Booking


class Booking(models.Model):
    name = models.CharField(max_length=50)
    phone = models.EmailField()
    email = models.IntegerField()
    person_number = models.IntegerField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.name
