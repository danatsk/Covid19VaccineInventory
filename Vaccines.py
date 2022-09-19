from Vaccine import Vaccine


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, vac):
        self._conn.execute("""
               INSERT INTO vaccines (id, date, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [vac.id, vac.date, vac.supplier_id, vac.quantity])

    def find(self, vaccine_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, date, supplier, quantity FROM vaccines WHERE id = ?
        """, [vaccine_id])
        return Vaccine(*c.fetchone())

    def next_vaccine_id(self):
        c = self._conn.cursor()
        c.execute("""
        SELECT MAX(id) FROM vaccines
        """)
        return c.fetchone()[0]+1

    def get_earliest_date_vaccines(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM vaccines
            ORDER BY date limit 1
        """)
        return c.fetchone()

    def remove_vaccine(self, vac_id):
        c = self._conn.cursor()
        c.execute("""
            DELETE FROM vaccines WHERE id =?
        """, [vac_id])

    def update_vaccine_quantity(self, vac_id, vac_new_quan):
        c = self._conn.cursor()
        c.execute("""
            UPDATE vaccines SET quantity=(?) WHERE id=(?)
        """, [vac_new_quan, vac_id])

    def get_total_inventory(self):
        c = self._conn.cursor()
        c.execute("""SELECT SUM(quantity) FROM vaccines""")
        return c.fetchone()[0]
