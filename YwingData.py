from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades, UpgradeTypes, Upgrades

exp = Expansions(name="Y-wing Expansion Pack")
exp.save()
print(exp)
xship= Ships(name="Y-wing", expansion=exp, quantity=1)
xship.save()
print(xship)
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Horton Salm',25,1,1),('Dutch Vander',23,1,1),('Gray Squadron Pilot',20,1,0),('Gold Squadron Pilot',18,1,0)]

upgrades={'Horton Salm':[(1,6),(2,3),(1,2),(1,11),(1,10)],
          'Dutch Vander':[(1,6),(2,3),(1,2),(1,11),(1,10)],
          'Gray Squadron Pilot':[(1,6),(2,3),(1,2),(1,11),(1,10)],
          'Gold Squadron Pilot':[(1,6),(2,3),(1,2),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)

#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('R2 Astromech','Astromech',1,1,0),
                 ('R5-D8', 'Astromech',3,1,1),
                 ('Proton Torpedoes','Torpedoes',4,2,0),
                 ('Ion Cannon Turret','Turret',5,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

        
print("All Pilots created")
print("Creation Complete!")
