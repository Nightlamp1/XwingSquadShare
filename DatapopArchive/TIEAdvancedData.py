from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

exp = Expansions(name="TIE Advanced Expansion Pack", wave="Wave 1")
exp.save()
print(exp)
xship= Ships(name="TIE Advanced",expansion=exp,quantity=1)
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Darth Vader',29,1,1),('Maarek Stele',27,1,1),('Storm Squadron Pilot',23,1,0),('Tempest Squadron Pilot',21,1,0)]

#(qty, upgrade_type)
upgrades={'Darth Vader':[(1,1),(1,4),(1,11),(1,10)],
          'Maarek Stele':[(1,1),(1,4),(1,11),(1,10)],
          'Storm Squadron Pilot':[(1,4),(1,11),(1,10)],
          'Tempest Squadron Pilot':[(1,4),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Squad Leader','Elite',2,1,1),
                 ('Expert Handling', 'Elite',2,1,0),
                 ('Swarm Tactics', 'Elite',2,1,0),
                 ('Cluster Missiles', 'Missles',4,1,0),
                 ('Concussion Missiles', 'Missles',4,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
