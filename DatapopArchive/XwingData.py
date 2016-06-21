from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes

exp = Expansions(name="X-Wing Expansion Pack")
exp.save()
print(exp)
xship= Ships(name="X-Wing",expansion=exp,quantity=1)
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Wedge Antilles',29,1,1),('Garven Dreis',26,1,1),('Red Squadron Pilot',23,1,0),('Rookie Pilot',21,1,0)]

upgrades={'Wedge Antilles':[(1,1),(1,2),(1,3),(1,11)],'Garven Dreis':[(1,2),(1,3),(1,11)],
          'Red Squadron Pilot':[(1,2),(1,3),(1,11)],'Rookie Pilot':[(1,2),(1,3),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


print("All Pilots created")
print("Creation Complete!")
