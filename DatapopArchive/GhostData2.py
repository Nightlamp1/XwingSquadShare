from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Rebels" #Add Faction Data
wave = "Wave 8" #Add Wave Data
exp = Expansions.objects.get(name="Ghost Expansion Pack") # Create expansion object
exp.save()
print(exp)
xship= Ships(name="Attack-Shuttle",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Hera Syndulla',22,1,1),('Sabine Wren',21,1,1),('Ezra Bridger',20,1,1),('Zeb Orrelios',18,1,1)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Hera Syndulla':[(1,1),(1,6),(1,8),(1,11),(1,10)],
          'Sabine Wren':[(1,1),(1,6),(1,8),(1,11),(1,10)],
          'Ezra Bridger':[(1,1),(1,6),(1,8),(1,11),(1,10)],
          'Zeb Orrelios':[(1,6),(1,8),(1,11),(1,10)]}

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
