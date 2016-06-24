from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
wave = "Wave 6" #Add Wave Data
exp = Expansions(name="M3-A Scyk Interceptor Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="M3-A-Interceptor",expansion=exp,quantity=2,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Laetin A\'Shera',18,1,1),('Serissu',20,1,1),('Tansarii Point Veteran',17,1,0),('Cartel Spacer',14,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Laetin A\'Shera':[(1,11),(1,10)],
          'Serissu':[(1,1),(1,11),(1,10)],
          'Tansarii Point Veteran':[(1,1),(1,11),(1,10)],
          'Cartel Spacer':[(1,11),(1,10)]}

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
                 ('Flechette Cannon', 'Cannon',2,1,0),
                 ('Ion Cannon', 'Cannon',3,1,0),
                 ('Heavy Scyk Interceptor', 'Title',2,1,0),
                 ('Stealth Device', 'Modification',3,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
