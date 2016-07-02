from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels" #Add Faction Data
wave = "Wave 8" #Add Wave Data
exp = Expansions(name="Ghost Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="VCX-100",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Hera Syndulla',40,1,1),('Kanan Jarrus',38,1,1),('Chopper',37,1,1),('Lothal Rebel',35,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Hera Syndulla':[(1,9),(1,6),(2,3),(2,8),(1,11),(1,10)],
          'Kanan Jarrus':[(1,9),(1,6),(2,3),(2,8),(1,11),(1,10)],
          'Chopper':[(1,9),(1,6),(2,3),(2,8),(1,11),(1,10)],
          'Lothal Rebel':[(1,9),(1,6),(2,3),(2,8),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Predator','Elite',3,1,0),
                 ('Advanced Proton Torpedoes', 'Torpedoes',6,1,0),
                 ('Dorsal Turret', 'Turret',3,2,0),
                 ('Cluster Mines', 'Bomb',4,1,0),
                 ('Conner Net', 'Bomb',4,1,0),
                 ('Thermal Detonators', 'Bomb',3,1,0),
                 ('Chopper', 'Crew',0,1,1),
                 ('Zeb Orrelios', 'Crew',1,1,1),
                 ('Ezra Bridger', 'Crew',3,1,1),
                 ('Hera Syndulla', 'Crew',1,1,1),
                 ('Kanan Jarrus', 'Crew',3,1,1),
                 ('Sabine Wren', 'Crew',2,1,1),
                 ('Ghost', 'Title',0,1,1),
                 ('Phantom', 'Title',0,1,1),
                 ('Reinforced Deflectors', 'System',3,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
