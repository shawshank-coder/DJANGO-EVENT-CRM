from django.db import models

# Create your models here.
class User(models.Model):
    GENDER = [
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    # active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    STATUS = [
        ('O', 'OPEN_BOOKING'),
        ('C', 'BOOKINGS_CLOSED'),
        ('X', 'EVENT CANCELLED'),
        ('Y', 'EVENT_COMPLETE')
    ]
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    desc = models.TextField()
    venue = models.CharField(max_length=30)
    crowdsize = models.IntegerField(default=50)
    bookedsize = models.IntegerField(default=0)
    price = models.IntegerField()
    num_of_ratings = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField(default=4)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feedback

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booked_at = models.DateField()

    def __str__(self):
        return 'Booking id: {}'.format(self.booking_id)


