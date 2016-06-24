from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Wave 5" #Add Wave Data
exp = Expansions(name="VT-49 Decimator Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="VT-49-Decimator",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Rear Admiral Chiraneau',46,1,1),('Commander Kenkirk',44,1,1),('Captain Oicunn',42,1,1),('Patrol Leader',40,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Rear Admiral Chiraneau':[(1,1),(1,3),(3,8),(1,7),(1,11),(1,10)],
          'Commander Kenkirk':[(1,1),(1,3),(3,8),(1,7),(1,11),(1,10)],
          'Captain Oicunn':[(1,1),(1,3),(3,8),(1,7),(1,11),(1,10)],
          'Patrol Leader':[(1,3),(3,8),(1,7),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Intimidation','Elite',2,1,0),
                 ('Ruthlessness', 'Elite',3,2,0),
                 ('Ion Torpedoes', 'Torpedoes',5,2,0),
                 ('Proton Bombs', 'Bomb',5,1,0),
                 ('Fleet Officer', 'Crew',3,1,0),
                 ('Mara Jade', 'Crew',3,1,1),
                 ('Moff Jerjerrod', 'Crew',2,1,1),
                 ('Ysanne Isard', 'Crew',4,1,1),
                 ('Dauntless', 'Title',2,1,1),
                 ('Tactical Jammers', 'Modification',1,2,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
