from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from .models import User

def getAllUsers(request):
    json_data = serializers.serialize('json', User.objects.all(), fields=('user_id', 'name', 'email', 'gender'))
    data = json.loads(json_data)
    for d in data:
        del d['pk']
        del d['model']
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json', status=200)
    

def createUser(request):
    data = json.loads(request.body)
    newuser = User(name=data['name'], email=data['email'], gender=data['gender'])
    newuser.save()
    return JsonResponse({'msg': 'User Created'}, status=201)


def getUserById(request, userid):
    user_obj = User.objects.filter(user_id=userid)
    print(user_obj)    
    if not user_obj:
        return JsonResponse({'error': 'User doesnot exist'})
    json_data = serializers.serialize('json', user_obj, fields=('user_id', 'name', 'email', 'gender'))
    data = json.loads(json_data)[0]
    del data['pk']
    del data['model']
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json', status=200)



def updateUserById(request, userid):
    updatedFields = json.loads(request.body)
    try:
        instance_obj = User.objects.get(pk=userid)
        if 'name' in updatedFields:
            instance_obj.name = updatedFields['name']
        if 'gender' in updatedFields:
            instance_obj.gender = updatedFields['gender']
        instance_obj.save()
        return JsonResponse({'msg': 'User Updated'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User doesnot exist'})
    # except User.MultipleObjectsReturned:
    #     return JsonResponse({'error': 'Multiple users exists with similar properties'})
    except:
        return JsonResponse({'error': 'Something went wrong'}, status=204)
    


def deleteUserById(request, userid):
    user_obj = User.objects.filter(user_id=userid)
    if not user_obj:
        print("No such user found")
        return JsonResponse({'msg': 'Invalid User ID'})
    user_obj.delete()
    return JsonResponse({'msg': 'User with id deleted'}, status=204)
    