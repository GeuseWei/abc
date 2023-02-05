from django.shortcuts import render, HttpResponse
from app1.models import User


# Create your views here.

def index(request):
    return HttpResponse("Hello")


def adduser(request):
    user = User()
    user.name = 'Mike'
    user.phone = 3333333333
    user.save()
    return HttpResponse('Add user successfully!')


def showusers(request):
    users = User.objects.all()
    for user in users:
        print(user.name + ' ' + str(user.gender))
    return HttpResponse('Check successfully!')


def updateuser(request):
    user = User.objects.get(name='Mike')
    user.gender = 'female'
    user.save()
    return HttpResponse('Update successfully!')


def deleteuser(request):
    user = User.objects.get(name='Jerry')
    user.delete()
    return HttpResponse('Delete successfully!')

