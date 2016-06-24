from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
wave = "Wave 6" #Add Wave Data
exp = Expansions(name="StarViper Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="StarViper",expansion=exp,quantity=2,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Prince Xizor',31,1,1),('Guri',30,1,1),('Black Sun Vigo',27,1,0),('Black Sun Enforcer',25,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Prince Xizor':[(1,1),(1,3),(1,11),(1,10)],
          'Guri':[(1,1),(1,3),(1,11),(1,10)],
          'Black Sun Vigo':[(1,3),(1,11)],
          'Black Sun Enforcer':[(1,3),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Bodyguard','Elite',2,1,1),
                 ('Calculation', 'Elite',1,1,0),
                 ('Ion Torpedoes', 'Torpedoes',5,1,0),
                 ('Accuracy Corrector', 'System',3,1,0),
                 ('Virago', 'Title',1,1,1),
                 ('Autothrusters', 'Modification',2,2,0),
                 ('Hull Upgrade', 'Modification',3,1,0),
                 ('Inertial Dampeners', 'Illicit',1,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
