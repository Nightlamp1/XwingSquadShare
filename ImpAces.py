from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Theme Pack" #Add Wave Data
exp = Expansions(name="Imperial Aces Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="TIE-Interceptor",expansion=exp,quantity=2,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Carnor Jax',26,1,1),('Tetran Cowall',24,1,1),('Kir Kanos',24,1,1),('Lieutenant Lorrir',23,1,1),('Royal Guard Pilot',22,2,0),('Saber Squadron Pilot',21,2,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Carnor Jax':[(1,1),(1,11),(1,10)],
          'Tetran Cowall':[(1,1),(1,11),(1,10)],
          'Kir Kanos':[(1,11),(1,10)],
          'Lieutenant Lorrir':[(1,11),(1,10)],
          'Royal Guard Pilot':[(1,1),(1,11),(1,10)],
          'Saber Squadron Pilot':[(1,1),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Opportunist','Elite',4,2,0),
                 ('Push the Limit', 'Elite',3,2,0),
                 ('Royal Guard TIE', 'Title',0,2,0),
                 ('Hull Upgrade', 'Modification',3,2,0),
                 ('Shield Upgrade', 'Modification',4,2,0),
                 ('Targeting Computer', 'Modification',2,2,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
