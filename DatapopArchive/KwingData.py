from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Empire" #Add Faction Data
wave = "Wave 7" #Add Wave Data
exp = Expansions(name="TIE Punisher Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="TIE-Punisher",expansion=exp,quantity=2,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Miranda Doni',29,1,1),('Esege Tuketu',28,1,1),('Guardian Squadron Pilot',25,1,0),('Warden Squadron Pilot',23,1,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'Miranda Doni':[(1,6),(2,3),(1,4),(1,8),(2,7),(1,11)],
          'Esege Tuketu':[(1,6),(2,3),(1,4),(1,8),(2,7),(1,11)],
          'Guardian Squadron Pilot':[(1,6),(2,3),(1,4),(1,8),(2,7),(1,11)],
          'Warden Squadron Pilot':[(1,6),(2,3),(1,4),(1,8),(2,7),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Extra Munitions','Torpedoes',2,1,0),
                 ('Plasma Torpedoes', 'Torpedoes',3,1,0),
                 ('Adv. Homing Missiles', 'Missles',3,1,0),
                 ('Twin Laser Turret', 'Turret',6,2,0),
                 ('Conner Net', 'Bomb',4,1,0),
                 ('Ion Bombs', 'Bomb',2,1,0),
                 ('Bombardier', 'Crew',1,1,0),
                 ('Advanced SLAM', 'Modification',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
