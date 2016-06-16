from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire"
exp = Expansions(name="TIE Interceptor Expansion Pack", wave="Wave 2")
exp.save()
print(exp)
xship= Ships(name="TIE-Interceptor",expansion=exp,quantity=1,faction=faction)
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Soontir Fel',27,1,1),('Turr Phennir',25,1,1),('Fel\'s Wrath',23,1,1),('Saber Squadron Pilot',21,1,0),('Avenger Squadron Pilot',20,1,0),('Alpha Squadron Pilot',18,1,0)]

#(qty, upgrade_type)
upgrades={'Soontir Fel':[(1,1),(1,11),(1,10)],
          'Turr Phennir':[(1,1),(1,11),(1,10)],
          'Fel\'s Wrath':[(1,11),(1,10)],
          'Saber Squadron Pilot':[(1,1),(1,11)],
          'Avenger Squadron Pilot':[(1,11)],
          'Alpha Squadron Pilot':[(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Daredevil','Elite',3,1,0),
                 ('Elusiveness', 'Elite',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
