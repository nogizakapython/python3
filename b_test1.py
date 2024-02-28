from bycycle import Bycycle
from bycycle_electrnic import ElectricBycycle

by1 = Bycycle("梅澤美波")
by1.setName = "山下美月"
driver_name1 = by1.getName
by1.ride()
by1.breaking()

by2 = Bycycle()
by2.setName = ""
driver_name2 = by2.getName
by2.ride()
by2.breaking()

eby = ElectricBycycle("")
eby.setName = "久保史緒里"
driver_name3 = eby.getName
eby.ride()
eby.breaking()
eby.electronic_ride()

