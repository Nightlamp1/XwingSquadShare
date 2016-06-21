from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Wave 4" #Add Wave Data
exp = Expansions(name="TIE Phantom Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="TIE-Phantom",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Whisper',32,1,1),('Echo',30,1,1),('Shadow Squadron Pilot',27,1,0),('Sigma Squadron Pilot',25,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Whisper':[(1,1),(1,9),(1,8),(1,11)],
          'Echo':[(1,1),(1,9),(1,8),(1,11)],
          'Shadow Squadron Pilot':[(1,9),(1,8),(1,11)],
          'Sigma Squadron Pilot':[(1,9),(1,8),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Recon Specialist','Crew',3,1,0),
                 ('Tactician', 'Crew',2,1,0),
                 ('Fire Control System', 'System',2,1,0),
                 ('Advanced Cloaking Device', 'Modification',4,1,0),
                 ('Stygium Particle Accelerator', 'Modification',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
