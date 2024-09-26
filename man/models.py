from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()  # This field will only have date, no time
    description = models.TextField()


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Anonymous')
    contact= models.CharField(max_length=200,default='contactnumber')
    booking_date=models.DateField(blank=True,null=False)
    email = models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking for {self.event.name} by {self.user.username}'


# Add this Feedback model
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contactnumber = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    
# models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, blank=True)
   
    def __str__(self):
        return self.user.username
