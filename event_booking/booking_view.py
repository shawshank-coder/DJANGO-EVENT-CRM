from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from .models import Booking
from .models import Event
from .models import Booking

# 

def getAllBookings(request):
    json_data = serializers.serialize('json', Booking.objects.all(), fields=('booking_id', 'user', 'event', 'booked_at'))
    data = json.loads(json_data)
    for d in data:
        del d['pk']
        del d['model']
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json', status=200)
    

def createBooking(request):
    data = json.loads(request.body)
    userid = data['userid']
    eventid = data['eventid']
    u = User.objects.filter(user_id=userid)
    e = Event.objects.filter(event_id=eventid)
    if e.bookedsize >= e.crowdsize:
        return JsonResponse({'msg': 'Show housefull'}, status=406)
    newBooking = Booking(user=u, event=e)
    newBooking.save()
    e.bookedsize += 1
    e.save()
    return JsonResponse({'msg': 'Booking Created'}, status=201)


def getBookingById(request, bookingid):
    booking_obj = Booking.objects.filter(booking_id=bookingid)
    print(booking_obj)    
    if not booking_obj:
        return JsonResponse({'error': 'Booking doesnot exist'})
    json_data = serializers.serialize('json', booking_obj, fields=('booking_id', 'user_id', 'event_id', 'booked_at'))
    data = json.loads(json_data)[0]
    del data['pk']
    del data['model']
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json', status=200)



# def updateBookingById(request, bookingid):
#     updatedFields = json.loads(request.body)
#     try:
#         instance_obj = Booking.objects.get(pk=bookingid)
#         if 'name' in updatedFields:
#             instance_obj.name = updatedFields['name']
#         if 'gender' in updatedFields:
#             instance_obj.gender = updatedFields['gender']
#         instance_obj.save()
#         return JsonResponse({'msg': 'Booking Updated'})
#     except Booking.DoesNotExist:
#         return JsonResponse({'error': 'Booking doesnot exist'})
#     # except Booking.MultipleObjectsReturned:
#     #     return JsonResponse({'error': 'Multiple Bookings exists with similar properties'})
#     except:
#         return JsonResponse({'error': 'Something went wrong'})
    


def deleteBookingById(request, bookingid):
    booking_obj = Booking.objects.filter(booking_id=bookingid)
    e = Event.objects.filter(user_id=booking_obj.event.event_id)
    if not booking_obj:
        print("No such Booking found")
        return JsonResponse({'msg': 'Invalid Booking ID'})
    booking_obj.delete()
    e.bookedsize -= 1
    e.save()
    return JsonResponse({'msg': 'Booking with id deleted'}, status=204)
    