from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Wave 3" #Add Wave Data
exp = Expansions(name="TIE-Bomber Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="TIE-Bomber",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Major Rhymer',26,1,1),('Captain Jonus',22,1,1),('Gamma Squadron Pilot',18,1,0),('Scimitar Squadron Pilot',16,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Major Rhymer':[(1,1),(2,3),(2,4),(1,7),(1,11)],
          'Captain Jonus':[(1,1),(2,3),(2,4),(1,7),(1,11)],
          'Gamma Squadron Pilot':[(2,3),(2,4),(1,7),(1,11)],
          'Scimitar Squadron Pilot':[(2,3),(2,4),(1,7),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Adrenaline Rush','Elite',1,1,0),
                 ('Advanced Proton Torpedoes', 'Torpedoes',6,1,0),
                 ('Assault Missiles', 'Missles',5,1,0),
                 ('Proton Bombs', 'Bomb',5,1,0),
                 ('Seismic Charges', 'Bomb',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
