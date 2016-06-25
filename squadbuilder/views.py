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
            selected_expansions=request.POST.getlist('expansionCode')
            selected_expansions_conversion = []
            for value in selected_expansions:
                x = value.split(",",2)
                y = []
                for num in x:
                    z=int(num)
                    y.append(z)
                selected_expansions_conversion.append(y)
            
            ships = []
            available_ships =[]
            available_pilots =[]
            all_pilots=[]
            upgradeList={}
            pilotCostDict={}
            upgradeCardDict={}
            for expansion in selected_expansions_conversion: #expansion[0]=expansion id, expansion[1]=quantity
                if int(expansion[1]) > 0:
                    ship_query = Ships.objects.all().filter(expansion=(expansion[0]))
                    for ship in ship_query:
                        ships.append({'name':ship.name, 'faction':ship.faction, 'quantity':ship.quantity*expansion[1], 'altFaction':ship.altFaction})
                        pilots = Pilots.objects.all().filter(expansion=(expansion[0]),ship=ship)
                        for pilot in pilots:
                            upgrades=[]
                            pilotID=pilot.name.replace(" ","")
                            pilotID=pilotID.replace("'","")
                            if pilot.faction == "Scum":
                                pilotID+="Scum"
                            all_pilots.append({'code':pilot.id,'id':pilotID,'name':pilot.name,'cost':pilot.pilotCost,'ship':pilot.ship.name,'quantity':pilot.quantity*expansion[1],'faction':pilot.faction})
                            upgrade_query = Pilot2Upgrades.objects.select_related('upgrade').filter(pilot=pilot)
                            for upgrade in upgrade_query:
                                if int(expansion[1]) > 1:
                                    pass
                                else:
                                    if upgrade.quantity > 1:
                                        for value in range(0,int(upgrade.quantity)):
                                            upgrades.append(upgrade.upgrade.name)
                                    else:
                                        upgrades.append(upgrade.upgrade.name)
                                
                                    #upgrades.append(upgrade[0])    
                                    upgradeList[pilotID]=upgrades
                                    pilotCostDict[pilotID]=pilot.pilotCost
                                
                types=list(UpgradeTypes.objects.all().values_list('name'))
                for upgradeType in types:
                    if int(expansion[1]) >0:
                        upgrade_builder={}
                        upgrade_attributes=list(Upgrades.objects.filter(upgradetype__name=upgradeType[0],expansion=(expansion[0])).values_list('name','upgradeCost','id'))
                        for attribute in upgrade_attributes:
                             upgrade_builder[attribute[0]]={'cost':attribute[1],'code':attribute[2]}
                        if upgradeType[0] in upgradeCardDict:
                            upgradeCardDict[upgradeType[0].replace(" ","")].update(upgrade_builder)
                        else:
                            upgradeCardDict[upgradeType[0].replace(" ","")]=upgrade_builder

            for ship in ships:
                if any(d['name']==ship['name'] for d in available_ships):
                    pass #add quantity addition here
                else:
                    available_ships.append(ship)

            for pilot in all_pilots:
                if any((d['name']==pilot['name'] and d['faction']==pilot['faction']) for d in available_pilots):
                    for entry in available_pilots:
                        if pilot['name']==entry['name'] and pilot['faction']==entry['faction']:
                            entry['quantity']+=pilot['quantity']
                else:
                    available_pilots.append(pilot)
                
            return render(request, 'squadbuilder/builder.html',{'ships':available_ships,'upgrades':json.dumps(upgradeList),
                                                                'pilotCost':json.dumps(pilotCostDict),
                                                                'cards':json.dumps(upgradeCardDict),
                                                                'pilots':available_pilots})
    else:
        exps = Expansions.objects.all()#will need to be owned expansions
        waves = Expansions.objects.order_by('wave').values_list('wave').distinct()
        return render(request, 'squadbuilder/selector.html',{'expansions':exps,'waves':waves})
        



 
        
    
