from django.shortcuts import render
from squadbuilder.models import Expansions,Pilots,Ships,Pilot2Upgrades, UpgradeTypes, Upgrades, UpgradeRestrictions, UpgradeBonus
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
            ship_objects =[]
            pilot_objects =[]
            available_pilots ={}
            available_ships={}
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
                            elif pilot.ship.name == "VCX-100":
                                pilotID+="VCX"
                            elif pilot.ship.name == "TIE-Defender":
                                pilotID+="Defender"
                            all_pilots.append({'code':pilot.id,'id':pilotID,'name':pilot.name,'cost':pilot.pilotCost,'ship':pilot.ship.name,'quantity':pilot.quantity*expansion[1],'faction':pilot.faction})
                            upgrade_query = Pilot2Upgrades.objects.select_related('upgrade').filter(pilot=pilot)
                            for upgrade in upgrade_query:
                                if upgrade.quantity > 1:
                                    for value in range(0,int(upgrade.quantity)):
                                        upgrades.append(upgrade.upgrade.name)
                                else:
                                    upgrades.append(upgrade.upgrade.name)
                                   
                                upgradeList[pilotID]=upgrades
                                pilotCostDict[pilotID]=pilot.pilotCost
                                
                types=list(UpgradeTypes.objects.all().values_list('name'))
                for upgradeType in types:
                    if int(expansion[1]) >0:
                        upgrade_builder={}
                        upgrade_attributes=list(Upgrades.objects.filter(upgradetype__name=upgradeType[0],expansion=(expansion[0])).values_list('name','upgradeCost','id','quantity'))
                        for attribute in upgrade_attributes:
                             upgrade_builder[attribute[0]]={'cost':attribute[1],'code':attribute[2],'quantity':attribute[3]*expansion[1]}
                             if upgradeType[0] in upgradeCardDict:
                                 if attribute[0] in upgradeCardDict[upgradeType[0]]:
                                     upgrade_builder[attribute[0]]['quantity']+=upgradeCardDict[upgradeType[0]][attribute[0]]['quantity']
                        if upgradeType[0] in upgradeCardDict:
                            upgradeCardDict[upgradeType[0].replace(" ","")].update(upgrade_builder)
                        else:
                            upgradeCardDict[upgradeType[0].replace(" ","")]=upgrade_builder

            #Building JSON list of ship objects to be used to populate builder and control squad building as needed
            for ship in ships:
                if any(d['name']==ship['name'] for d in ship_objects):
                    available_ships[ship['name']]['quantity']+=ship['quantity']
                else:
                    ship_objects.append(ship)
                    available_ships[ship['name']]=ship

            #Building JSON list of pilot objects to be used to populate builder and control squad building as needed
            for pilot in all_pilots:
                if any((d['name']==pilot['name'] and d['faction']==pilot['faction'] and d['ship']==pilot['ship']) for d in pilot_objects):
                    for entry in pilot_objects:
                        if pilot['name']==entry['name'] and pilot['faction']==entry['faction']:
                            entry['quantity']+=pilot['quantity']
                            print(pilot)
                            available_pilots[pilot['id']]['quantity']+=pilot['quantity']
                else:
                    pilot_objects.append(pilot)
                    available_pilots[pilot['id']]={'quantity':pilot['quantity'],'faction':pilot['faction'],'ship':pilot['ship'], 'code':pilot['code'], 'cost':pilot['cost'], 'name':pilot['name']}

            #Building JSON list of restriction objects to be used to limit what upgrade cards are visible to the user
            upgrade_restrictions = {}
            restriction_query = UpgradeRestrictions.objects.all()
            for restriction in restriction_query:
                upgrade_restrictions[restriction.upgrade]={'restriction':restriction.restriction,'type':restriction.restriction_type}

            #Building JSON list of upgrade bonus objects to be used to populate any additional effects given by upgrade cards
            upgrade_bonus = {}
            bonus_query = UpgradeBonus.objects.all()
            for bonus in bonus_query:
                if bonus.upgrade in upgrade_bonus:
                    upgrade_bonus[bonus.upgrade]['bonus'].append(bonus.bonus.name)
                else:
                    upgrade_bonus[bonus.upgrade]={'type':bonus.bonus_type, 'quantity':bonus.bonus_quantity, 'bonus':[bonus.bonus.name]}
                    if bonus.bonus_quantity > 1:
                        for item in range(1,bonus.bonus_quantity):
                            upgrade_bonus[bonus.upgrade]['bonus'].append(bonus.bonus.name)
                            
                
            return render(request, 'squadbuilder/builder.html',{'ships':ship_objects,'upgrades':json.dumps(upgradeList),
                                                                'pilotCost':json.dumps(pilotCostDict),
                                                                'cards':json.dumps(upgradeCardDict),
                                                                'pilots':pilot_objects,
                                                                'available_pilots':json.dumps(available_pilots),
                                                                'available_ships':json.dumps(available_ships),
                                                                'upgrade_restrictions':json.dumps(upgrade_restrictions),
                                                                'upgrade_bonus':json.dumps(upgrade_bonus)})
    else:
        exps = Expansions.objects.all()
        waves = Expansions.objects.order_by('wave').values_list('wave').distinct()
        return render(request, 'squadbuilder/selector.html',{'expansions':exps,'waves':waves})
        



 
        
    
