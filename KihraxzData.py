from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
wave = "Wave 7" #Add Wave Data
exp = Expansions(name="Kihraxz Fighter Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="Kihraxz-Fighter",expansion=exp,quantity=2,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Talonbane Cobra',28,1,1),('Graz The Hunter',25,1,1),('Black Sun Ace',23,1,0),('Cartel Marauder',20,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Talonbane Cobra':[(1,1),(1,4),(1,12),(1,11)],
          'Graz The Hunter':[(1,4),(1,12),(1,11)],
          'Black Sun Ace':[(1,1),(1,4),(1,12),(1,11)],
          'Cartel Marauder':[(1,4),(1,12),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Crack Shot','Elite',1,1,0),
                 ('Lightning Reflexes', 'Elite',1,1,0),
                 ('Predator', 'Elite',3,1,0),
                 ('Homing Missiles', 'Missles',5,1,0),
                 ('Glitterstim', 'Illicit',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
