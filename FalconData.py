from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels"
exp = Expansions(name="Millennium Falcon Expansion Pack", wave="Wave 2")
exp.save()
print(exp)
xship= Ships(name="YT-1300",expansion=exp,quantity=1,faction=faction)
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Han Solo',46,1,1),('Lando Calrissian',44,1,1),('Chewbacca',42,1,1),('Outer Rim Smuggler',27,1,0)]

#(qty, upgrade_type)
upgrades={'Han Solo':[(1,1),(1,4),(2,8),(1,11),(1,10)],
          'Lando Calrissian':[(1,1),(1,4),(2,8),(1,11),(1,10)],
          'Chewbacca':[(1,1),(1,4),(2,8),(1,11),(1,10)],
          'Outer Rim Smuggler':[(2,8),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Draw Their Fire','Elite',1,1,0),
                 ('Elusiveness', 'Elite',2,1,0),
                 ('Veteran Instincts', 'Elite',1,1,0),
                 ('Assault Missiles', 'Missles',5,1,0),
                 ('Concussion Missiles', 'Missles',4,1,0),
                 ('Chewbacca', 'Crew',4,1,1),
                 ('Luke Skywalker', 'Crew',7,1,1),
                 ('Nien Nunb', 'Crew',1,1,1),
                 ('Weapons Engineer', 'Crew',3,1,0),
                 ('Millennium Falcon', 'Title',4,1,0),
                 ('Engine Upgrade', 'Modification',4,2,0),
                 ('Shield Upgrade', 'Modification',4,2,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
