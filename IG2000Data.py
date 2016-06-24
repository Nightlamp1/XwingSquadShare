from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
wave = "Wave 6" #Add Wave Data
exp = Expansions(name="IG-2000 Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="Aggressor-assault-fighter",expansion=exp,quantity=2,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('IG-88A',36,1,1),('IG-88B',36,1,1),('IG-88C',36,1,1),('IG-88D',36,1,1)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'IG-88A':[(1,1),(1,9),(2,5),(1,7),(1,12),(1,11),(1,10)],
          'IG-88B':[(1,1),(1,9),(2,5),(1,7),(1,12),(1,11),(1,10)],
          'IG-88C':[(1,1),(1,9),(2,5),(1,7),(1,12),(1,11),(1,10)],
          'IG-88D':[(1,1),(1,9),(2,5),(1,7),(1,12),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Mangler Cannon','Cannon',4,1,0),
                 ('Autoblaster', 'Cannon',5,1,0),
                 ('Proximity Mines', 'Bomb',3,1,0),
                 ('Seismic Charges', 'Bomb',2,1,0),
                 ('Accuracy Corrector', 'System',3,1,0),
                 ('IG-2000', 'Title',0,1,0),
                 ('Hot Shot Blaster', 'Illicit',3,1,0),
                 ('Dead Man\'s Switch', 'Illicit',2,2,0),
                 ('Feedback Array', 'Illicit',2,2,0),
                 ('Inertial Dampeners', 'Illicit',1,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
