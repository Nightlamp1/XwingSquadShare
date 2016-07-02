from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
wave = "Wave 8" #Add Wave Data
exp = Expansions(name="Mist Hunter Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="G-1A-Starfighter",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Zuckuss',28,1,1),('4-LOM',27,1,1),('Gand Findsman',25,1,0),('Ruthless Freelancer',23,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Zuckuss':[(1,1),(1,8),(1,9),(1,12),(1,11),(1,10)],
          '4-LOM':[(1,1),(1,8),(1,9),(1,12),(1,11),(1,10)],
          'Gand Findsman':[(1,1),(1,8),(1,9),(1,12),(1,11),(1,10)],
          'Ruthless Freelancer':[(1,8),(1,9),(1,12),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Adaptability','Elite',0,2,0),
                 ('4-LOM', 'Crew',1,1,1),
                 ('Zuckuss', 'Crew',1,1,1),
                 ('Tractor Beam', 'Cannon',1,1,0),
                 ('Mist Hunter', 'Title',0,1,1),
                 ('Electronic Baffle', 'System',1,2,0),
                 ('Cloaking Device', 'Illicit',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
