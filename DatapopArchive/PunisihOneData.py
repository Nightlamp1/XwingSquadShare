from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
wave = "Wave 8" #Add Wave Data
exp = Expansions(name="Punishing One Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="JumpMaster-5000",expansion=exp,quantity=1,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Dengar',33,1,1),('Tel Trevura',30,1,1),('Manaroo',27,1,1),('Contracted Scout',25,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Dengar':[(1,1),(2,3),(1,8),(1,17),(1,12),(1,11),(1,10)],
          'Tel Trevura':[(1,1),(2,3),(1,8),(1,17),(1,12),(1,11),(1,10)],
          'Manaroo':[(1,1),(2,3),(1,8),(1,17),(1,12),(1,11),(1,10)],
          'Contracted Scout':[(1,1),(2,3),(1,8),(1,17),(1,12),(1,11),(1,10)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Rage','Elite',1,1,0),
                 ('Attanni Mindlink', 'Elite',1,2,0),
                 ('Plasma Torpedoes', 'Torpedoes',3,1,0),
                 ('Gonk', 'Crew',2,1,1),
                 ('Boba Fett', 'Crew',1,1,1),
                 ('Dengar', 'Crew',3,1,1),
                 ('R5-P8', 'Salvaged Astromech',3,1,1),
                 ('Overclocked R4', 'Salvaged Astromech',1,2,0),
                 ('Punishing One', 'Title',12,1,1),
                 ('Guidance Chips', 'Modification',0,2,0),
                 ('Feedback Array', 'Illicit',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
