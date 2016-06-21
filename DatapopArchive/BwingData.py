from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels" #Add Faction Data
wave = "Wave 3" #Add Wave Data
exp = Expansions(name="B-wing Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="B-wing",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Ten Numb',31,1,1),('Ibtisam',28,1,1),('Dagger Squadron Pilot',24,1,0),('Blue Squadron Pilot',22,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Ten Numb':[(1,1),(1,9),(1,5),(2,3),(1,11),(1,10)],
          'Ibtisam':[(1,1),(1,9),(1,5),(2,3),(1,11),(1,10)],
          'Dagger Squadron Pilot':[(1,9),(1,5),(2,3),(1,11),(1,10)],
          'Blue Squadron Pilot':[(1,9),(1,5),(2,3),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Advanced Proton Torpedoes','Torpedoes',6,1,0),
                 ('Proton Torpedoes', 'Torpedoes',4,1,0),
                 ('Autoblaster', 'Cannon',5,1,0),
                 ('Ion Cannon', 'Cannon',3,1,0),
                 ('Fire Control System', 'Modification',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")