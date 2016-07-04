from squadbuilder.models import UpgradeTypes, UpgradeBonus

additions = [('B-Wing E2','None','Crew',1),
             ('A-Wing Test Pilot','None','Elite',1),
             ('TIE x7','remove','Cannon',1),
             ('TIE x7','remove','Missles',1),
             ('TIE Shuttle','remove','Torpedoes',2),
             ('TIE Shuttle','remove','Missles',2),
             ('TIE Shuttle','remove','Bomb',1),
             ('TIE Shuttle','None','Crew',2),
             ('Royal Guard TIE','None','Modification',1)]


for entry in additions:
    upgrade_type = UpgradeTypes.objects.get(name=entry[2])
    print("{} as {} for {} and {}".format(entry[0],entry[1],entry[2],entry[3]))
    bonus = UpgradeBonus(upgrade=entry[0],bonus_type=entry[1],bonus=upgrade_type,bonus_quantity=entry[3])
    print(bonus.upgrade)
    bonus.save()
