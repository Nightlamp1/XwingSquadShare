from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Wave 8" #Add Wave Data
exp = Expansions(name="Inquisitor\'s TIE Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="TIE-Advanced-Prototype",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('The Inquisitor',25,1,1),('Valen Rudor',22,1,1),('Baron of the Empire',19,1,0),('Sienar Test Pilot',16,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'The Inquisitor':[(1,1),(1,4),(1,11),(1,10)],
          'Valen Rudor':[(1,1),(1,4),(1,11),(1,10)],
          'Baron of the Empire':[(1,1),(1,4),(1,11),(1,10)],
          'Sienar Test Pilot':[(1,4),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Deadeye','Elite',1,1,0),
                 ('Homing Missiles', 'Missles',5,1,0),
                 ('XX-23 S-Thread Tracers', 'Missles',1,2,0),
                 ('Guidance Chips', 'Modification',0,1,0),
                 ('TIE-v1', 'Title',1,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
