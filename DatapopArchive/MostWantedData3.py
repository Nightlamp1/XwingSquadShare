from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
exp = Expansions.objects.get(name='Most Wanted Expansion Pack')
print(exp)

xship= Ships.objects.get(name='Firespray-31') # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Boba Fett',39,1,1),('Kath Scarlett',38,1,1),('Emon Azzameen',36,1,0),('Mandalorian Mercenary',35,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Boba Fett':[(1,1),(1,5),(1,7),(1,8),(1,4),(1,12),(1,11),(1,10)],
          'Kath Scarlett':[(1,1),(1,5),(1,7),(1,8),(1,4),(1,12),(1,11),(1,10)],
          'Emon Azzameen':[(1,5),(1,7),(1,8),(1,4),(1,12),(1,11),(1,10)],
          'Mandalorian Mercenary':[(1,5),(1,7),(1,8),(1,4),(1,12),(1,11),(1,10)]}

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

