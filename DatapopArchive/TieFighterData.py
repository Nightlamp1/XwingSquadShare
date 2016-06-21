from squadbuilder.models import Expansions, Ships, Pilots, Pilot2Upgrades, UpgradeTypes, Upgrades

exp = Expansions(name="TIE Fighter Expansion Pack")
exp.save()
print(exp)
xship= Ships(name="Tie-Fighter", expansion=exp, quantity=1)
xship.save()
print(xship)
print("Expansions and Ships created")
print("Starting Pilot Creation")

xpilots=[('Howlrunner',18,1,1),('Backstabber',16,1,1),('Winged Gundark',15,1,1),('Black Squadron Pilot',14,1,0),('Obsidian Squadron Pilot',13,1,0),('Academy Pilot',12,1,0)]

upgrades={'Howlrunner':[(1,1),(1,11)],
          'Backstabber':[(1,11)],
          'Winged Gundark':[(1,11)],
          'Black Squadron Pilot':[(1,1),(1,11)],
          'Obsidian Squadron Pilot':[(1,11)],
          'Academy Pilot':[(1,11)]}

for pilot in xpilots:
    temp = Pilots(name=pilot[0],pilotCost=pilot[1],quantity=pilot[2],isUnique=pilot[3],expansion=exp,ship=xship)
    print(temp)
    temp.save()
    for pilot_upgrade in upgrades[pilot[0]]:
        p_upgrades = Pilot2Upgrades(pilot=temp,quantity=pilot_upgrade[0],upgrade=UpgradeTypes.objects.get(id=pilot_upgrade[1]))
        p_upgrades.save()
        print(p_upgrades)

#card= ('Title','Type',cost,quantity,unique(1 or 0))
upgrade_cards = [('Determination','Elite',1,1,0),
                 ('Swarm Tactics', 'Elite',2,1,0)]

for card in upgrade_cards:
    card_insert = Upgrades(name=card[0],upgradetype=UpgradeTypes.objects.get(name=card[1]),upgradeCost=card[2],expansion=exp,quantity=card[3],isUnique=card[4])
    print card_insert.name
    card_insert.save()

        
print("All Pilots created")
print("Creation Complete!")
