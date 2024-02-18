from bycycle import Bycycle
from bycycle_electrnic import ElectricBycycle

by1 = Bycycle("梅澤美波")
by1.setName = "山下美月"
driver_name1 = by1.getName
by1.riding(driver_name1)
by1.breaking(driver_name1)

by2 = Bycycle()
by2.setName = ""
driver_name2 = by2.getName
by2.riding(driver_name2)
by2.breaking(driver_name2)

eby = ElectricBycycle()
eby.setName = "久保史緒里"
driver_name3 = eby.getName
eby.riding(driver_name3)
eby.breaking(driver_name3)
eby.electronic_ride(driver_name3)

