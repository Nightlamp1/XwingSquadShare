from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Wave 8" #Add Wave Data
exp = Expansions(name="TIE/fo Fighter Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="TIE-Fighter-First-Order",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Omega Leader',21,1,1),('Zeta Leader',20,1,1),('Epsilon Ace',17,1,1),('Omega Squadron Pilot',17,2,0),('Zeta Squadron Pilot',16,2,0),('Epsilon Squadron Pilot',15,2,0)] #list pilots


#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Omega Leader':[(1,1),(1,13),(1,11)],
          'Zeta Leader':[(1,1),(1,13),(1,11)],
          'Epsilon Ace':[(1,13),(1,11)],
          'Omega Squadron Pilot':[(1,1),(1,13),(1,11)],
          'Zeta Squadron Pilot':[(1,13),(1,11)],
          'Epsilon Squadron Pilot':[(1,13),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Juke','Elite',2,1,0),
                 ('Comm Relay', 'Tech',3,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
