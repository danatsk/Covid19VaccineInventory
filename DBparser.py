import Clinic
import Logistic
import Repository
import Supplier
import Vaccine
import Dao
from Repository import repo


def parse(config_file):
    repo.create_tables()
    with open(config_file) as file:
        amounts = file.readline()
        amounts.strip()
        vaccinesBulk = int(amounts[0])
        suppliersAmount = int(amounts[2])
        clinicsAmount = int(amounts[4])
        logisticsAmount = int(amounts[6])
        for i in range(0, vaccinesBulk):
            line = file.readline()
            line = line.split(",")
            vac = Vaccine.Vaccine(int(line[0]), line[1], int(line[2]), int(line[3]))
            repo.Vaccines.insert(vac)
        for i in range(vaccinesBulk, vaccinesBulk + suppliersAmount):
            line = file.readline()
            line = line.split(",")
            sup = Supplier.Supplier(int(line[0]), line[1], int(line[2]))
            repo.Suppliers.insert(sup)
            # Dao.Dao.insert(sup,Supplier)
        for i in range(suppliersAmount, suppliersAmount + clinicsAmount):
            line = file.readline()
            line = line.split(",")
            clinc = Clinic.Clinic(int(line[0]), line[1], int(line[2]), int(line[3]))
            repo.Clinics.insert(clinc)
        for i in range(clinicsAmount, clinicsAmount + logisticsAmount):
            line = file.readline()
            line = line.split(",")
            logi = Logistic.Logistic(int(line[0]), line[1], int(line[2]), int(line[3]))
            repo.Logistics.insert(logi)


class DBparser:
    # def __init__(self):
    #     # DBparser = self

    pass
