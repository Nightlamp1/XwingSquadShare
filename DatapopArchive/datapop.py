from squadbuilder.models import Expansions, Ships, Pilots

exp = Expansions(name="A-Wing Expansion Pack")
exp.save()
xship= Ships(name="A-Wing",expansion=exp,quantity=1)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Tycho Celchu',26,1,1),('Arvel Crynyd',23,1,1),
         ('Green Squadron Pilot',19,1,0),('Prototype Pilot',17,1,0)]


for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship)
    temp.save()

print("All Pilots created")
print("Creation Complete!")
