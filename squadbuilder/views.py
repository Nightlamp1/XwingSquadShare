from django.shortcuts import render
from squadbuilder.models import Expansions,Pilots,Ships,Pilot2Upgrades, UpgradeTypes, Upgrades
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from squadbuilder.forms import LoginForm
import json


# Create your views here.
def index(request):
    return render(request, 'squadbuilder/home.html')

def contact(request):
    return render(request, 'squadbuilder/basic.html',{'content':['If you would like to contact me:',
                                                             'robert.britt2011@gmail.com']})
def squadbuilder(request):
    ships = Ships.objects.all()
    exps = Expansions.objects.all()#will need to be owned expansions
    shipList =[]
    upgradeList={}
    pilotCostDict={}
    upgradeCardDict={}
    for item in ships:
        pilots = Pilots.objects.filter(ship=item)
        shipList.append((item.name,pilots))
        for pilot in pilots:
            upgrades=[]
            pilotID=pilot.name.replace(" ","")
            upgrade_query = list(UpgradeTypes.objects.filter(pilot2upgrades__pilot=pilot).values_list('name'))
            for upgrade in upgrade_query:
                upgrades.append(upgrade[0])    
            upgradeList[pilotID]=upgrades
            pilotCostDict[pilotID]=pilot.pilotCost
    types=list(UpgradeTypes.objects.all().values_list('name'))
    for upgradeType in types:
        placeHolderDict={}
        placeHolder=list(Upgrades.objects.filter(upgradetype__name=upgradeType[0]).values_list('name','upgradeCost'))
        for item in placeHolder:
            placeHolderDict[item[0]]={'cost':item[1]}
        upgradeCardDict[upgradeType[0]]=placeHolderDict
    return render(request, 'squadbuilder/builder.html',{'ships':shipList,'upgrades':json.dumps(upgradeList),
                                                        'pilotCost':json.dumps(pilotCostDict),
                                                        'cards':json.dumps(upgradeCardDict),
                                                        'expansions':exps})

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

def selector(request):
    exps = Expansions.objects.all()#will need to be owned expansions
    return render(request, 'squadbuilder/selector.html',{'expansions':exps})
    
