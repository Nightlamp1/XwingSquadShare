from squadbuilder.models import UpgradeRestrictions

additions=[('B-Wing E2','B-wing','ship'),
           ('A-Wing Test Pilot','A-Wing','ship'),
           ('Kyle Katarn','Rebels','faction'),
           ('Jan Ors','Rebels','faction'),
           ('Chardaan Refit','A-Wing','ship'),
           ('TIE x7','TIE-Defender','ship'),
           ('TIE D','TIE-Defender','ship'),
           ('TIE Shuttle','TIE-Bomber','ship'),
           ('Systems Officer','Empire','faction'),
           ('Royal Guard TIE','TIE-Interceptor','ship')]

for upgrade in additions:
    sql_add = UpgradeRestrictions(upgrade=upgrade[0],restriction=upgrade[1],restriction_type=upgrade[2])
    sql_add.save()
    print(sql_add.upgrade)
