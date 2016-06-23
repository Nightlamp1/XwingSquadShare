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
            cost = request.POST['cost']
            current_user = request.user
            new_squad = SavedSquads(name=squadname, user=current_user, squadcode=squadcode, upvotes=0, cost=cost)
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
                        pilots = Pilots.objects.all().filter(expansion=(index+1))
                        for pilot in pilots:
                            upgrades=[]
                            pilotID=pilot.name.replace(" ","")
                            if pilot.faction == "Scum":
                                pilotID+="Scum"
                            all_pilots.append({'code':pilot.id,'id':pilotID,'name':pilot.name,'cost':pilot.pilotCost,'ship':pilot.ship.name,'quantity':pilot.quantity,'faction':pilot.faction})
                            upgrade_query = list(UpgradeTypes.objects.filter(pilot2upgrades__pilot=pilot).values_list('name'))
                            for upgrade in upgrade_query:
                                upgrades.append(upgrade[0])    
                                upgradeList[pilotID]=upgrades
                                pilotCostDict[pilotID]=pilot.pilotCost
                                
                types=list(UpgradeTypes.objects.all().values_list('name'))
                for upgradeType in types:
                    if int(quantity) >0:
                        upgrade_builder={}
                        upgrade_attributes=list(Upgrades.objects.filter(upgradetype__name=upgradeType[0],expansion=(index+1)).values_list('name','upgradeCost','id'))
                        for attribute in upgrade_attributes:
                             upgrade_builder[attribute[0]]={'cost':attribute[1],'code':attribute[2]}
                        if upgradeType[0] in upgradeCardDict:
                            upgradeCardDict[upgradeType[0].replace(" ","")].update(upgrade_builder)
                        else:
                            upgradeCardDict[upgradeType[0].replace(" ","")]=upgrade_builder

            for ship in ships:
                if any(d['name']==ship.name for d in available_ships):
                    pass #add quantity addition here
                else:
                    available_ships.append({'name':ship.name, 'faction':ship.faction, 'quantity':ship.quantity, 'altFaction':ship.altFaction})

            for pilot in all_pilots:
                if any((d['name']==pilot['name'] and d['faction']==pilot['faction']) for d in available_pilots):
                    pass #add quantity addition here
                else:
                    available_pilots.append(pilot)
                
            #need to revisit to apply filter by expansion
            '''types=list(UpgradeTypes.objects.filter(expansion=(index+1)).values_list('name'))
            for upgradeType in types:
                upgrade_builder={}
                upgrade_attributes=list(Upgrades.objects.filter(upgradetype__name=upgradeType[0]).values_list('name','upgradeCost','id'))
                for attribute in upgrade_attributes:
                     upgrade_builder[attribute[0]]={'cost':attribute[1],'code':attribute[2]}
                upgradeCardDict[upgradeType[0]]=upgrade_builder'''
            return render(request, 'squadbuilder/builder.html',{'ships':available_ships,'upgrades':json.dumps(upgradeList),
                                                                'pilotCost':json.dumps(pilotCostDict),
                                                                'cards':json.dumps(upgradeCardDict),
                                                                'pilots':available_pilots})
    else:
        exps = Expansions.objects.all()#will need to be owned expansions
        return render(request, 'squadbuilder/selector.html',{'expansions':exps})
        



 
        
    
