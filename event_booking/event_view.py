from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from .models import Event
import datetime

def getAllEvents(request):
    json_data = serializers.serialize('json', Event.objects.all(), fields=('event_id', 'name', 'desc', 'venue', 'price', 'num_of_ratings'))
    data = json.loads(json_data)
    for d in data:
        del d['pk']
        del d['model']
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json', status=200)
    

def createEvent(request):
    data = json.loads(request.body)
    newEvent = Event(name=data['name'], desc=data['desc'], venue=data['venue'], price=data['price'], status=data['status'])
    if crowdsize in data: 
        newEvent.crowdsize = data['crowdsize']
    newEvent.save()
    return JsonResponse({'msg': 'Event Created'}, status=201)


def getEventById(request, eventid):
    event_obj = Event.objects.filter(event_id=eventid)   
    if not event_obj:
        return JsonResponse({'error': 'Event doesnot exist'})
    json_data = serializers.serialize('json', event_obj, fields=('event_id', 'name', 'desc', 'venue', 'price', 'num_of_ratings'))
    data = json.loads(json_data)[0]
    del data['pk']
    del data['model']
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json', status=200)



def updateEventById(request, eventid):
    updatedFields = json.loads(request.body)
    try:
        instance_obj = Event.objects.get(pk=eventid)
        if 'name' in updatedFields:
            instance_obj.name = updatedFields['name']
        if 'desc' in updatedFields:
            instance_obj.desc = updatedFields['desc']
        if 'venue' in updatedFields:
            instance_obj.venue = updatedFields['venue']
        if 'price' in updatedFields:
            instance_obj.price = updatedFields['price']
        if 'crowdsize' in updatedFields:
            instance_obj.crowdsize = updatedFields['crowdsize']
        instance_obj.updated_at = datetime.datetime.now()
        instance_obj.save()
        return JsonResponse({'msg': 'Event Updated'})
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event doesnot exist'})
    except:
        return JsonResponse({'error': 'Something went wrong'}, status=204)
    


def deleteEventById(request, Eventid):
    event_obj = Event.objects.filter(event_id=Eventid)
    if not event_obj:
        print("No such Event found")
        return JsonResponse({'msg': 'Invalid Event ID'})
    event_obj.delete()
    return JsonResponse({'msg': 'Event with id deleted'}, status=204)
    