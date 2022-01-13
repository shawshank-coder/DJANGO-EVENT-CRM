from django.contrib import admin
from .models import User
from .models import Event
from .models import Review
from .models import Booking


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'email', 'gender']


class EventAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'name', 'desc', 'price', 'crowdsize', 'bookedsize', 'num_of_ratings']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event', 'rating', 'feedback']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'user', 'event', 'booked_at']


admin.site.register(User, UserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Booking, BookingAdmin)
