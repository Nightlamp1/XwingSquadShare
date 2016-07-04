from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Theme Pack" #Add Wave Data
exp = Expansions.objects.get(name="Imperial Veterans Expansion Pack") # Create expansion object
exp.save()
print(exp)
xship= Ships(name="TIE-Bomber",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Tomax Bren',24,1,1),('Deathfire',17,1,1),('Gamma Squadron Veteran',19,2,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Tomax Bren':[(1,1),(2,3),(2,4),(1,7),(1,11),(1,10)],
          'Deathfire':[(2,3),(2,4),(1,7),(1,11),(1,10)],
          'Gamma Squadron Veteran':[(1,1),(2,3),(2,4),(1,7),(1,11),(1,10)]}

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
