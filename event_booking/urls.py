from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.users, name='all users'),
    path('users/<int:userid>', views.userbyid, name='user by id'),
    path('events/', views.events, name='get or create events'),
    path('events/<int:eventid>', views.eventbyid, name='event by id'),
    path('reviews/', views.reviews, name='get or create review'),
    path('reviews/<int:reviewid>', views.reviewbyid, name='review by id'),
    path('bookings/', views.bookings, name='all users'),
    path('bookings/<int:bookingid>', views.bookingbyid, name='booking by id'),
]