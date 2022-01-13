from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from .models import Review
from .models import Event
from .models import User

def getAllReviews(request):
    json_data = serializers.serialize('json', Review.objects.all(), fields=('review_id', 'user', 'event', 'rating', 'feedback'))
    data = json.loads(json_data)
    for d in data:
        del d['pk']
        del d['model']
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json', status=200)
    

def createReview(request):
    data = json.loads(request.body)
    userid = data['userid']
    eventid = data['eventid']
    u = User.objects.filter(user_id=userid)
    e = Event.objects.filter(event_id=eventid) 
    newReview = Review(user=u, event=e, rating=data['rating'], feedback=data['feedback'])
    newReview.save()
    u.num_of_ratings += 1
    u.save()
    return JsonResponse({'msg': 'Review Created'}, status=201)


def getReviewById(request, reviewid):
    review_obj = Review.objects.filter(review_id=reviewid)
    print(review_obj)    
    if not review_obj:
        return JsonResponse({'error': 'Review doesnot exist'})
    json_data = serializers.serialize('json', review_obj, fields=('review_id', 'user', 'event', 'rating', 'feedback'))
    data = json.loads(json_data)[0]
    del data['pk']
    del data['model']
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json', status=200)



def updateReviewById(request, reviewid):
    updatedFields = json.loads(request.body)
    try:
        instance_obj = review.objects.get(pk=reviewid)
        if 'userid' in updatedFields:
            return JsonResponse({'error': 'User attribute cannot be updated'}) 
        if 'eventid' in updatedFields:
            return JsonResponse({'error': 'Event attribute cannot be updated'}) 
        if 'rating' in updatedFields:
            instance_obj.rating = updatedFields['rating']
        if 'feedback' in updatedFields:
            instance_obj.feedback = updatedFields['feedback']
        instance_obj.save()
        return JsonResponse({'msg': 'Review Updated'})
    except Review.DoesNotExist:
        return JsonResponse({'error': 'Review doesnot exist'})
    # except Review.MultipleObjectsReturned:
    #     return JsonResponse({'error': 'Multiple Reviews exists with similar properties'})
    except:
        return JsonResponse({'error': 'Something went wrong'}, status=204)
    


def deleteReviewById(request, reviewid):
    review_obj = review.objects.filter(review_id=reviewid)
    u = User.objects.filter(user_id=review_obj.user.user_id)
    if not review_obj:
        print("No such Review found")
        return JsonResponse({'msg': 'Invalid Review ID'})
    review_obj.delete()
    u.num_of_ratings -= 1
    u.save()
    return JsonResponse({'msg': 'Review with id deleted'}, status=204)
    