from squadbuilder.models import UpgradeTypes, UpgradeBonus

additions = [('Andrasta','None','Bomb',2),
             ('Bomb Loadout','None','Bomb',1),
             ('Heavy Scyk Interceptor','or','Cannon',1),
             ('Heavy Scyk Interceptor','or','Torpedoes',1),
             ('Heavy Scyk Interceptor','or','Missles',1),
             ('Sabine Wren','None','Bomb',1),
             ('Slave 1','None','Torpedoes',1),
             ('Virago','and','System',1),
             ('Virago','and','Illicit',1)]

for entry in additions:
    upgrade_type = UpgradeTypes.objects.get(name=entry[2])
    print("{} as {} for {} and {}".format(entry[0],entry[1],entry[2],entry[3]))
    bonus = UpgradeBonus(upgrade=entry[0],bonus_type=entry[1],bonus=upgrade_type,bonus_quantity=entry[3])
    print(bonus.upgrade)
    bonus.save()
