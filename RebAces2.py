from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels" #Add Faction Data
wave = "Theme Pack" #Add Wave Data
exp = Expansions.objects.get(name="Rebel Aces Expansion Pack") # Create expansion object
exp.save()
print(exp)
xship= Ships(name="A-wing",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Jake Farrell',24,1,1),('Gemmer Sojan',22,1,1),('Green Squadron Pilot',19,1,0),('Prototype Pilot',17,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Jake Farrell':[(1,1),(1,4),(1,11),(1,10)],
          'Gemmer Sojan':[(1,4),(1,11),(1,10)],
          'Green Squadron Pilot':[(1,1),(1,4),(1,11),(1,10)],
          'Prototype Pilot':[(1,4),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)



print("All Pilots created")
print("Creation Complete!")
