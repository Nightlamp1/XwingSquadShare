from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
exp = Expansions.objects.get(name='Most Wanted Expansion Pack')
print(exp)

xship= Ships.objects.get(name='HWK-290') # Create ship object
print(xship)
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Dace Bonearm',23,1,1),('Palob Godalhi',20,1,1),('Torkil Mux',19,1,1),('Spice Runner',16,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Dace Bonearm':[(1,1),(1,6),(1,8),(1,12),(1,11),(1,10)],
          'Palob Godalhi':[(1,1),(1,6),(1,8),(1,12),(1,11),(1,10)],
          'Torkil Mux':[(1,6),(1,8),(1,12),(1,11),(1,10)],
          'Spice Runner':[(1,6),(1,8),(1,12),(1,11),(1,10)]}

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

