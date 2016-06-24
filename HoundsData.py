from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
wave = "Wave 7" #Add Wave Data
exp = Expansions(name="Hound\'s Tooth Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="YV-666-freighter",expansion=exp,quantity=2,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Bossk',35,1,1),('Latts Razzi',33,1,1),('Moralo Eval',34,1,1),('Trandoshan Slaver',29,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Bossk':[(1,1),(1,5),(1,4),(3,8),(1,12),(1,11),(1,10)],
          'Latts Razzi':[(1,5),(1,4),(3,8),(1,12),(1,11),(1,10)],
          'Moralo Eval':[(1,5),(1,4),(3,8),(1,12),(1,11),(1,10)],
          'Trandoshan Slaver':[(1,5),(1,4),(3,8),(1,12),(1,11),(1,10)]}

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
                 ('Lone Wolf', 'Elite',2,1,1),
                 ('Stay on Target', 'Elite',2,1,0),
                 ('Heavy Laser Cannon', 'Cannon',7,1,0),
                 ('Bossk', 'Crew',2,1,1),
                 ('K4 Security Droid', 'Crew',3,1,0),
                 ('Outlaw Tech', 'Crew',2,1,0),
                 ('Hound\'s Tooth', 'Title',6,1,1),
                 ('Engine Upgrade', 'Modification',4,1,0),
                 ('Ion Projector', 'Modification',2,2,0),
                 ('Maneuvering Fins', 'Modification',1,1,0),
                 ('Glitterstim', 'Illicit',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
