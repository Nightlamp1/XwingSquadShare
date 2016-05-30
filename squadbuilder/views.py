from django.shortcuts import render
from squadbuilder.models import Expansions,Pilots,Ships,Pilot2Upgrades, UpgradeTypes, Upgrades
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
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
    if request.method == 'POST':
        selected_expansions=request.POST['expansionCode']
        ships = []
        available_ships =[]
        available_pilots =[]
        all_pilots=[]
        upgradeList={}
        pilotCostDict={}
        upgradeCardDict={}
        for index, quantity in enumerate(selected_expansions):
            if int(quantity) > 0:
                ship_query = Ships.objects.all().filter(expansion=(index+1))
                for ship in ship_query:
                    ships.append(ship)
                    pilots = Pilots.objects.filter(ship=ship, expansion=(index+1))
                    for pilot in pilots:
                        upgrades=[]
                        pilotID=pilot.name.replace(" ","")
                        all_pilots.append({'id':pilotID,'name':pilot.name,'cost':pilot.pilotCost,'ship':ship.name,'quantity':pilot.quantity,'faction':pilot.faction})
                        upgrade_query = list(UpgradeTypes.objects.filter(pilot2upgrades__pilot=pilot).values_list('name'))
                        for upgrade in upgrade_query:
                            upgrades.append(upgrade[0])    
                            upgradeList[pilotID]=upgrades
                            pilotCostDict[pilotID]=pilot.pilotCost

        for ship in ships:
            if any(d['name']==ship.name for d in available_ships):
                pass #add quantity addition here
            else:
                available_ships.append({'name':ship.name, 'faction':ship.faction, 'quantity':ship.quantity})

        for pilot in all_pilots:
            if any(d['name']==pilot['name'] for d in available_pilots):
                pass #add quantity addition here
            else:
                available_pilots.append(pilot)
            
        #need to revisit to apply filter by expansion
        types=list(UpgradeTypes.objects.all().values_list('name'))
        for upgradeType in types:
            placeHolderDict={}
            placeHolder=list(Upgrades.objects.filter(upgradetype__name=upgradeType[0]).values_list('name','upgradeCost'))
            for item in placeHolder:
                 placeHolderDict[item[0]]={'cost':item[1]}
            upgradeCardDict[upgradeType[0]]=placeHolderDict
        return render(request, 'squadbuilder/builder.html',{'ships':available_ships,'upgrades':json.dumps(upgradeList),
                                                            'pilotCost':json.dumps(pilotCostDict),
                                                            'cards':json.dumps(upgradeCardDict),
                                                            'pilots':available_pilots})
    else:
        exps = Expansions.objects.all()#will need to be owned expansions
        return render(request, 'squadbuilder/selector.html',{'expansions':exps})
        

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

 
        
    
