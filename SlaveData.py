from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire"
exp = Expansions(name="Slave 1 Expansion Pack", wave="Wave 2")
exp.save()
print(exp)
xship= Ships(name="Firespray-31",expansion=exp,quantity=1,faction=faction)
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Boba Fett',39,1,1),('Kath Scarlet',38,1,1),('Krassis Trelix',36,1,1),('Bounty Hunter',33,1,0)]

#(qty, upgrade_type)
upgrades={'Boba Fett':[(1,1),(1,5),(1,7),(1,8),(1,4),(1,11),(1,10)],
          'Kath Scarlet':[(1,1),(1,5),(1,7),(1,8),(1,4),(1,11),(1,10)],
          'Krassis Trelix':[(1,5),(1,7),(1,8),(1,4),(1,11),(1,10)],
          'Bounty Hunter':[(1,5),(1,7),(1,8),(1,4),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Expose','Elite',4,1,0),
                 ('Veteran Instincts', 'Elite',1,1,0),
                 ('Assault Missiles', 'Missles',5,1,0),
                 ('Homing Missiles', 'Missles',5,1,0),
                 ('Heavy Laser Cannon', 'Cannon',7,1,0),
                 ('Ion Cannon', 'Cannon',3,1,0),
                 ('Proximity Mines', 'Bomb',3,1,0),
                 ('Seismic Charges', 'Bomb',2,1,0),
                 ('Gunner', 'Crew',5,1,0),
                 ('Mercenary Copilot', 'Crew',2,1,0),
                 ('Slave 1', 'Title',0,1,1),
                 ('Stealth Device', 'Modification',3,2,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
