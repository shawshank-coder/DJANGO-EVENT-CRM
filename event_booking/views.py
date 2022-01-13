from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .user_view import getAllUsers, createUser, getUserById, updateUserById, deleteUserById
from .event_view import getAllEvents, createEvent, getEventById, updateEventById, deleteEventById
from .review_view import getAllReviews, createReview, getReviewById, updateReviewById, deleteReviewById
from .booking_view import getAllBookings, createBooking, getBookingById, deleteBookingById

# Create your views here.
@csrf_exempt
def users(request):
    if request.method == 'GET':
        return getAllUsers(request)
    if request.method == 'POST':
        return createUser(request) 

@csrf_exempt
def userbyid(request, userid):
    if request.method == 'GET':
        return getUserById(request, userid)
    if request.method == 'PUT':
        return updateUserById(request, userid)
    if request.method == 'DELETE':
        return deleteUserById(request, userid)


@csrf_exempt
def events(request):
    if request.method == 'GET':
        return getAllEvents(request)
    if request.method == 'POST':
        return createEvent(request)

@csrf_exempt
def eventbyid(request, eventid):
    if request.method == 'GET':
        return getEventById(request, eventid)
    if request.method == 'PUT':
        return updateEventById(request, eventid)
    if request.method == 'DELETE':
        return deleteEventById(request, eventid) 


@csrf_exempt
def reviews(request):
    if request.method == 'GET':
        return getAllReviews(request)
    if request.method == 'POST':
        return createReview(request)


@csrf_exempt
def reviewbyid(request, reviewid):
    if request.method == 'GET':
        return getReviewById(request, reviewid)
    if request.method == 'PUT':
        return updateReviewById(request, reviewid)
    if request.method == 'DELETE':
        return deleteReviewById(request, reviewid) 


@csrf_exempt
def bookings(request):
    if request.method == 'GET':
        return getAllBookings(request)
    if request.method == 'POST':
        return createBooking(request)


@csrf_exempt
def bookingbyid(request, bookingid):
    if request.method == 'GET':
        return getBookingById(request, bookingid)
    # if request.method == 'PUT':
    #     return JsonResponse({'msg': 'Update a booking by id'}) 
    elif request.method == 'DELETE':
        return deleteBookingById(request, bookingid)  
    else:
        return JsonResponse({'msg': 'Invalid Path'}, status=400) 
    
