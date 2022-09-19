from Clinic import Clinic


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Clinic):
        self._conn.execute("""
               INSERT INTO clinics (id, location, demand, logistic) VALUES (?, ?, ?, ?)
           """, [Clinic.id, Clinic.location, Clinic.demand, Clinic.logistic_id])

    def find(self, clinic_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, location, demand, logistic FROM clinics WHERE id = ?
        """, [clinic_id])
        return Clinic(*c.fetchone())

    def get_clinic_id(self, clinic_location):
        c = self._conn.cursor()
        c.execute("""
            SELECT id FROM clinics WHERE location = ?
        """, [clinic_location])
        return c.fetchone()[0]

    def get_clinic_logistic(self, clinic_location):
        c = self._conn.cursor()
        c.execute("""
            SELECT logistic FROM clinics WHERE location = ?
        """, [clinic_location])
        return c.fetchone()[0]

    def get_demand(self, clinic_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT demand FROM clinics WHERE id = ?
        """, [clinic_id])
        return c.fetchone()[0]

    def update_demand(self, clinic_id, amount):
        old_demand = self.get_demand(clinic_id)
        new_amount = old_demand-amount
        c = self._conn.cursor()
        c.execute("""
            UPDATE clinics SET demand=(?) WHERE id=(?)
        """, [new_amount, clinic_id])

    def get_total_demand(self):
        c = self._conn.cursor()
        c.execute("""SELECT SUM(demand) FROM clinics""")
        return c.fetchone()[0]
