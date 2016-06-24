from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
exp = Expansions.objects.get(name='Most Wanted Expansion Pack')
print(exp)

xship= Ships(name="Y-Wing",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Kavil',24,1,1),('Drea Renthal',22,1,1),('Hired Gun',20,2,0),('Syndicate Thug',18,2,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Kavil':[(1,1),(1,6),(2,3),(1,17),(1,11),(1,10)],
          'Drea Renthal':[(1,6),(2,3),(1,17),(1,11),(1,10)],
          'Hired Gun':[(1,6),(2,3),(1,17),(1,11),(1,10)],
          'Syndicate Thug':[(1,6),(2,3),(1,17),(1,11),(1,10)]}

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

