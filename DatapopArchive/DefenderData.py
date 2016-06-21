from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Wave 4" #Add Wave Data
exp = Expansions(name="TIE Phantom Expansion Pack", wave=wave) # Create expansion object
#exp.save()
print(exp)
xship= Ships(name="TIE-Phantom",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
#xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Rexler Brath',37,1,1),('Colonel Vessery',35,1,1),('Onyx Squadron Pilot',32,1,0),('Delta Squadron Pilot',30,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Rexler Brath':[(1,1),(1,5),(1,4),(1,11),(1,10)],
          'Colonel Vessery':[(1,1),(1,5),(1,4),(1,11),(1,10)],
          'Onyx Squadron Pilot':[(1,5),(1,4),(1,11),(1,10)],
          'Delta Squadron Pilot':[(1,5),(1,4),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    #temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        #p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Outmaneuver','Elite',3,1,0),
                 ('Predator', 'Elite',3,1,0),
                 ('Ion Cannon', 'Cannon',3,1,1),
                 ('Ion Pulse Missiles', 'Missles',3,1,0),
                 ('Munitions Failsafe', 'Modification',1,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    #card_insert.save()

print("All Pilots created")
print("Creation Complete!")
