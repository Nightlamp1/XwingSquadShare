from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels" #Add Faction Data
wave = "Wave 4" #Add Wave Data
exp = Expansions(name="Z-95 Headhunter Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="Z-95-Headhunter",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Airen Cracken',19,1,1),('Lieutenant Blount',17,1,1),('Tala Squadron Pilot',13,1,0),('Bandit Squadron Pilot',12,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Airen Cracken':[(1,1),(1,4),(1,11)],
          'Lieutenant Blount':[(1,1),(1,4),(1,11)],
          'Tala Squadron Pilot':[(1,4),(1,11)],
          'Bandit Squadron Pilot':[(1,4),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Decoy','Elite',2,1,0),
                 ('Wingman', 'Elite',2,1,0),
                 ('Ion Pulse Missiles', 'Missles',3,1,0),
                 ('Assault Missiles', 'Missles',5,1,0),
                 ('Munitions Failsafe', 'Modification',1,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
