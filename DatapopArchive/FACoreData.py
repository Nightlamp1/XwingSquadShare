from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels" #Add Faction Data
wave = "Core Set" #Add Wave Data
exp = Expansions(name="The Force Awakens Core Set", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="T-70 X-wing",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Poe Dameron',31,1,1),('Blue Ace',27,1,1),('Red Squadron Veteran',26,1,0),('Blue Squadron Novice',24,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Poe Dameron':[(1,1),(1,3),(1,2),(1,13),(1,11),(1,10)],
          'Blue Ace':[(1,3),(1,2),(1,13),(1,11)],
          'Red Squadron Veteran':[(1,1),(1,3),(1,2),(1,13),(1,11)],
          'Blue Squadron Novice':[(1,3),(1,2),(1,13),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('BB-8','Astromech',2,1,1),
                 ('R5-X3', 'Astromech',1,1,1),
                 ('Wired', 'Elite',1,1,0),
                 ('Weapons Guidance', 'Tech',2,1,0),
                 ('Proton Torpedoes', 'Torpedoes',4,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
