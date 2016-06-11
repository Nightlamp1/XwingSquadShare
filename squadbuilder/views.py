from django.shortcuts import render
from squadbuilder.models import Expansions,Pilots,Ships,Pilot2Upgrades, UpgradeTypes, Upgrades
from squadshare.models import SavedSquads
import json


# Create your views here.


def squadbuilder(request):
    if request.method == 'POST':
        squadcode = request.POST.get('squadcode', "")
        if squadcode!="":
            squadname = request.POST.get('squadname',"Unnamed Squad")
            current_user = request.user
            new_squad = SavedSquads(name=squadname, user=current_user, squadcode=squadcode, upvotes=0)
            new_squad.save()
            #squadname cleanup here in the future
            return render(request, 'squadbuilder/squadviewer.html',{'squadcode':squadcode,'squadname':squadname})
        else:
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
                            all_pilots.append({'code':pilot.id,'id':pilotID,'name':pilot.name,'cost':pilot.pilotCost,'ship':ship.name,'quantity':pilot.quantity,'faction':pilot.faction})
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
                placeHolder=list(Upgrades.objects.filter(upgradetype__name=upgradeType[0]).values_list('name','upgradeCost','id'))
                for item in placeHolder:
                     placeHolderDict[item[0]]={'cost':item[1],'code':item[2]}
                upgradeCardDict[upgradeType[0]]=placeHolderDict
            return render(request, 'squadbuilder/builder.html',{'ships':available_ships,'upgrades':json.dumps(upgradeList),
                                                                'pilotCost':json.dumps(pilotCostDict),
                                                                'cards':json.dumps(upgradeCardDict),
                                                                'pilots':available_pilots})
    else:
        exps = Expansions.objects.all()#will need to be owned expansions
        return render(request, 'squadbuilder/selector.html',{'expansions':exps})
        



 
        
    
