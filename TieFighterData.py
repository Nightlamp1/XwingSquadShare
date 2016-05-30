from squadbuilder.models import Expansions, Ships, Pilots

exp = Expansions(name="TIE Fighter Expansion Pack")
exp.save()
xship= Ships.objects.filter(id=2)
#xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Howlrunner',18,1,1),('Backstabber',16,1,1),('Winged Gundark',15,1,1),('Black Squadron Pilot',14,1,0),('Obsidian Squadron Pilot',13,1,0),('Academy Pilot',12,1,0)]


for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship)
    temp.save()

print("All Pilots created")
print("Creation Complete!")
