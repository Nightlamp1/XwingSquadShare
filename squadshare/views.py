from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from squadbuilder.forms import LoginForm
from squadshare.models import SavedSquads
from squadbuilder.models import Pilots, Upgrades

# Create your views here.
def index(request):

    def squadReader(squad_query):
        squad_readout = []
        for squad in squad_query:
            query_array=[]
            pilot_list =[]
            squadcode = squad.squadcode
            squadcode = squadcode.split('p')
            for item in squadcode:
                if item == "":
                     pass
                else:
                    query_array.append(item.split('u'))
            for query in query_array:
                upgrade_array=[]
                pilot_dict=[]
                for index, query_id in enumerate(query):
                    if index == 0:
                        pilot = Pilots.objects.get(id=query_id)
                        pilot_dict.append(pilot.name)
                    else:
                        upgrade = Upgrades.objects.get(id=query_id)
                        upgrade_array.append(upgrade.name)
                pilot_dict.append(upgrade_array)
                pilot_list.append(pilot_dict)
            squad_readout.append({'name':squad.name ,'list':pilot_list})
        return squad_readout
    recent_squads = SavedSquads.objects.all().order_by('createdDate')[:5]
    squad_list = squadReader(recent_squads)    
    return render(request, 'squadshare/home.html', {'recent_squads':recent_squads,'squad_list':squad_list})


            
            

def contact(request):
    return render(request, 'squadshare/basic.html',{'content':['If you would like to contact me:',
                                                             'robert.britt2011@gmail.com']})

#Break out into seperate app?
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'squadshare/basic.html',{'content':["Registration Successful"]})
        else:
            return render(request, 'squadshare/basic.html', {'content':["Failed Registration"]})
    else:
        form = UserCreationForm()
        c={}
        c.update(csrf(request))
        c['form'] = form
        return render(request, 'squadshare/register.html',c)
    
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
                return render(request, 'squadshare/basic.html', {'content':["Login successful"]})
            else:
                return render(request, 'squadshare/basic.html', {'content':["Failed Login"]})
        else:
            return render(request, 'squadshare/basic.html', {'content':["failed login"]})
    else:
        c={}
        c.update(csrf(request))
        return render(request, 'squadshare/login.html',c)

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')


def profile(request, username):
        user = User.objects.get(username=username)
        user_squads = SavedSquads.objects.filter(user=user)
        return render(request, 'squadshare/profile.html', {'user_squads':user_squads})
