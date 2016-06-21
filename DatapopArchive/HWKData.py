from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels"
wave = "Wave 3"
exp = Expansions(name="HWK-290 Expansion Pack", wave=wave)
exp.save()
print(exp)
xship= Ships(name="HWK-290",expansion=exp,quantity=1,faction=faction)
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Jan Ors',25,1,1),('Kyle Katarn',21,1,1),('Roark Garnet',19,1,1),('Rebel Operative',16,1,0)]

#(qty, upgrade_type)
upgrades={'Jan Ors':[(1,1),(1,6),(1,8),(1,11),(1,10)],
          'Kyle Katarn':[(1,1),(1,6),(1,8),(1,11),(1,10)],
          'Roark Garnet':[(1,6),(1,8),(1,11),(1,10)],
          'Rebel Operative':[(1,6),(1,8),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Blaster Turret','Turret',4,1,0),
                 ('Ion Cannon Turret', 'Turret',5,1,0),
                 ('Intelligence Agent', 'Crew',1,1,0),
                 ('Recon Specialist', 'Crew',3,1,0),
                 ('Saboteur', 'Crew',2,1,0),
                 ('Moldy Crow', 'Title',3,1,1)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
