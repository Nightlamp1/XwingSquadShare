from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades,UpgradeTypes, Upgrades

faction = "Scum" #Add Faction Data
wave = "Wave 6" #Add Wave Data
exp = Expansions(name="Most Wanted Expansion Pack", wave=wave) # Create expansion object
exp.save()
print(exp)
xship= Ships(name="Z-95-Headhunter",expansion=exp,quantity=2,faction=faction) # Create ship object
print(xship)
xship.save()
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('N\'dru Suhlak',17,1,1),('Kaat\'o Leeachos',15,1,1),('Black Sun Soldier',13,2,0),('Binayre Pirate',12,2,0)] #list pilots

#(qty, upgrade_type) -- Pilot2Upgrades link
upgrades={'N\'dru Suhlak':[(1,1),(1,4),(1,12),(1,11)],
          'Kaat\'o Leeachos':[(1,1),(1,4),(1,12),(1,11)],
          'Black Sun Soldier':[(1,4),(1,12),(1,11)],
          'Binayre Pirate':[(1,4),(1,12),(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship,faction=faction)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)


#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Autoblaster Turret','Turret',2,2,0),
                 ('Bomb Loadout', 'Torpedoes',0,2,0),
                 ('Greedo', 'Crew',1,1,1),
                 ('K4 Security Droid', 'Crew',3,1,0),
                 ('Outlaw Tech', 'Crew',2,1,0),
                 ('Genius', 'Salvaged Astromech',0,1,1),
                 ('R4 Agromech', 'Salvaged Astromech',2,2,0),
                 ('R4-B11', 'Salvaged Astromech',3,1,1),
                 ('Salvaged Astromech', 'Salvaged Astromech',2,2,0),
                 ('Unhinged Astromech', 'Salvaged Astromech',1,2,0),
                 ('BTL-A4 Y-wing', 'Title',0,2,0),
                 ('Andrasta', 'Title',0,1,1),
                 ('Hot Shot Blaster', 'Illicit',3,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

print("All Pilots created")
print("Creation Complete!")
