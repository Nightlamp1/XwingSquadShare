from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Theme Pack" #Add Wave Data
exp = Expansions(name="Imperial Veterans Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="TIE-Defender",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Maarek Stele',35,1,1),('Countess Ryad',34,1,1),('Glaive Squadron Pilot',34,2,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Maarek Stele':[(1,1),(1,5),(1,4),(1,11),(1,10)],
          'Countess Ryad':[(1,1),(1,5),(1,4),(1,11),(1,10)],
          'Glaive Squadron Pilot':[(1,1),(1,5),(1,4),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Proximity Mines','Bomb',3,1,0),
                 ('Cluster Mines', 'Bomb',4,1,0),
                 ('Tractor Beam', 'Cannon',1,1,0),
                 ('Systems Officer', 'Crew',2,1,0),
                 ('Crack Shot', 'Elite',1,1,0),
                 ('TIE x7', 'Title',-2,2,0),
                 ('TIE D', 'Title',0,2,0),
                 ('TIE Shuttle', 'Title',0,2,0),
                 ('Long Range Scanners', 'Modification',0,2,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
