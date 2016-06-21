from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire"
wave = "Wave 3"
exp = Expansions(name="Lambda-class Shuttle Expansion Pack", wave=wave)
exp.save()
print(exp)
xship= Ships(name="Lambda-class-Shuttle",expansion=exp,quantity=1,faction=faction)
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Captain Kagi',27,1,1),('Captain Yorr',24,1,1),('Colonel Jendon',26,1,1),('Omicron Group Pilot',21,1,0)]

#(qty, upgrade_type)
upgrades={'Captain Kagi':[(1,9),(1,5),(2,8),(1,11),(1,10)],
          'Captain Yorr':[(1,9),(1,5),(2,8),(1,11),(1,10)],
          'Colonel Jendon':[(1,9),(1,5),(2,8),(1,11),(1,10)],
          'Omicron Group Pilot':[(1,9),(1,5),(2,8),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Heavy Laser Cannon','Cannon',7,1,0),
                 ('Darth Vader', 'Crew',3,1,1),
                 ('Flight Instructor', 'Crew',4,1,0),
                 ('Intelligence Agent', 'Crew',1,1,0),
                 ('Navigator', 'Crew',3,1,0),
                 ('Rebel Captive', 'Crew',3,1,1),
                 ('Weapons Engineer', 'Crew',3,1,0),
                 ('Anti Pursuit Laser', 'Modification',2,2,0),
                 ('ST 321', 'Title',3,1,1),
                 ('Advanced Sensors', 'System',3,1,0),
                 ('Sensor Jammer', 'System',4,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
