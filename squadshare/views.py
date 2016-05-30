from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from squadbuilder.forms import LoginForm

# Create your views here.
def index(request):
    return render(request, 'squadshare/home.html')

def contact(request):
    return render(request, 'squadbuilder/basic.html',{'content':['If you would like to contact me:',
                                                             'robert.britt2011@gmail.com']})

#Break out into seperate app?
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/squadbuilder/home.html')
        else:
            return render(request, 'squadbuilder/basic.html', {'content':["Failed Registration"]})
    else:
        form = UserCreationForm()
        c={}
        c.update(csrf(request))
        c['form'] = form
        return render(request, 'squadbuilder/register.html',c)
    
#Break out into seperate app?
@csrf_protect
def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return render(request, 'squadbuilder/basic.html', {'content':["Login successful"]})
            else:
                return render(request, 'squadbuilder/basic.html', {'content':["Failed Login"]})
        else:
            return render(request, 'squadbuilder/basic.html', {'content':["failed login"]})
    else:
        c={}
        c.update(csrf(request))
        return render(request, 'squadbuilder/login.html',c)

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')
