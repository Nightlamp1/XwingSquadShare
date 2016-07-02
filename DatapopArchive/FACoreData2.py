from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Core Set" #Add Wave Data
exp = Expansions.objects.get(id=28)

print(exp)
xship= Ships(name="TIE/fo Fighter",expansion=exp,quantity=2,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Omega Ace',20,1,1),('Epsilon Leader',19,1,1),('Zeta Ace',18,1,1),('Omega Squadron Pilot',17,2,0),('Zeta Squadron Pilot',16,2,0),('Epsilon Squadron Pilot',15,2,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Omega Ace':[(1,1),(1,13),(1,11)],
          'Epsilon Leader':[(1,13),(1,11)],
          'Zeta Ace':[(1,1),(1,13),(1,11)],
          'Omega Squadron Pilot':[(1,1),(1,13),(1,11)],
          'Zeta Squadron Pilot':[(1,13),(1,11)],
          'Epsilon Squadron Pilot':[(1,13),(1,11)]}

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
