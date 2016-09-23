from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels" #Add Faction Data
wave = "Theme Pack" #Add Wave Data
exp = Expansions(name="Rebel Aces Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="B-wing",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Keyan Farlander',29,1,1),('Nera Dantels',26,1,1),('Dagger Squadron Pilot',24,1,0),('Blue Squadron Pilot',22,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Keyan Farlander':[(1,1),(1,9),(1,5),(2,3),(1,11)],
          'Nera Dantels':[(1,1),(1,9),(1,5),(2,3),(1,11)],
          'Dagger Squadron Pilot':[(1,9),(1,5),(2,3),(1,11)],
          'Blue Squadron Pilot':[(1,9),(1,5),(2,3),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Chardaan Refit','Missles',-2,3,0),
                 ('Proton Rockets', 'Missles',3,2,0),
                 ('Jan Ors', 'Crew',2,1,1),
                 ('Kyle Katarn', 'Crew',3,1,1),
                 ('Enhanced Scopes', 'System',1,2,0),
                 ('A-Wing Test Pilot', 'Title',0,2,0),
                 ('B-Wing E2', 'Modification',1,2,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
