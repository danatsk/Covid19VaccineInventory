import atexit
import sqlite3
import Vaccines
import Suppliers
import Clinics
import Logistics
import Dao
from Vaccine import Vaccine

con = sqlite3.connect('database.db')


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.Vaccines = Vaccines._Vaccines(self._conn)
        self.Suppliers = Suppliers._Suppliers(self._conn)
        self.Clinics = Clinics._Clinics(self._conn)
        self.Logistics = Logistics._Logistics(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
                   CREATE TABLE logistics (
                   id INT PRIMARY KEY,
                   name STRING NOT NULL,
                   count_sent INT NOT NULL,
                   count_received INT NOT NULL
                   );

                   CREATE TABLE suppliers (
                   id  INT    PRIMARY KEY,
                   name     STRING    NOT NULL,
                   logistic INT REFERENCES logistics(id)
                   );

                   CREATE TABLE vaccines (
                   id INT PRIMARY KEY,
                   date DATE NOT NULL,
                   supplier INT REFERENCES suppliers(id),
                   quantity INT NOT NULL
                   );

                   CREATE TABLE clinics (
                   id      INT     PRIMARY KEY,
                   location  STRING     NOT NULL,
                   demand           INT     NOT NULL,
                   logistic    INT    REFERENCES logistics(id)
                   );
           """)

    def get_next_vaccine_id(self):
        return self.Vaccines.next_vaccine_id()

    def get_supplier_logistic(self, supplier_id):
        return self.Suppliers.get_logistic(supplier_id)

    def get_clinic_logistic(self, clinic_location):
        return self.Clinics.get_clinic_logistic(clinic_location)

    def get_supplier_id(self, supplier_name):
        return self.Suppliers.get_id(supplier_name)

    def insert_vaccine(self, vac):
        self.Vaccines.insert(vac)

    def update_count_received(self, amount, supplier_name):
        logistic_id = self.get_supplier_logistic(self.get_supplier_id(supplier_name))
        self.Logistics.update_count_received(logistic_id, amount)

    def update_count_sent(self, amount, logistic_id):
        self.Logistics.update_count_sent(logistic_id, amount)

    def get_clinic_id(self, clinic_location):
        return self.Clinics.get_clinic_id(clinic_location)

    def get_earliest_vaccine(self):
        vac = self.Vaccines.get_earliest_date_vaccines()
        vac = Vaccine(*vac)
        return vac

    def get_clinic_demand(self, clinic_id):
        return self.Clinics.get_demand(clinic_id)

    def update_clinic_demand(self, clinic_location, amount):
        clinic_id = self.get_clinic_id(clinic_location)
        self.Clinics.update_demand(clinic_id, amount)

    def remove_vaccines(self, vac_id):
        self.Vaccines.remove_vaccine(vac_id)

    def update_vaccines_quantity(self, vac_id, vac_new_quan):
        self.Vaccines.update_vaccine_quantity(vac_id, vac_new_quan)

    def get_total_inventory(self):
        return self.Vaccines.get_total_inventory()

    def get_total_demand(self):
        return self.Clinics.get_total_demand()

repo = _Repository()
atexit.register(repo._close)
