from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels" #Add Faction Data
wave = "Wave 5" #Add Wave Data
exp = Expansions(name="YT-2400 Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="YT-2400",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Dash Rendar',36,1,1),('Leebo',34,1,1),('Eaden Vrill',32,1,1),('Wild Space Fringer',30,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Dash Rendar':[(1,1),(1,5),(1,4),(1,8),(1,11),(1,10)],
          'Leebo':[(1,1),(1,5),(1,4),(1,8),(1,11),(1,10)],
          'Eaden Vrill':[(1,5),(1,4),(1,8),(1,11),(1,10)],
          'Wild Space Fringer':[(1,5),(1,4),(1,8),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Lone Wolf','Elite',2,1,1),
                 ('Stay on Target', 'Elite',2,1,0),
                 ('Proton Rockets', 'Missles',3,1,0),
                 ('Heavy Laser Cannon', 'Cannon',7,1,0),
                 ('Leebo', 'Crew',2,1,1),
                 ('Dash Rendar', 'Crew',2,1,1),
                 ('Gunner', 'Crew',5,1,0),
                 ('Lando Calrissian', 'Crew',3,1,1),
                 ('Mercenary Copilot', 'Crew',2,1,0),
                 ('Outrider', 'Title',5,1,1),
                 ('Countermeasures', 'Modification',3,2,0),
                 ('Experimental Interface', 'Modification',3,1,1)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
