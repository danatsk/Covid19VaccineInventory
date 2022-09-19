from Clinic import Clinic


class _Logistics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Logistic):
        self._conn.execute("""
               INSERT INTO logistics (id, name, count_sent, count_received) VALUES (?, ?, ?, ?)
           """, [Logistic.id, Logistic.name, Logistic.count_sent, Logistic.count_received])

    # def find(self, logistic_id):
    #     c = self._conn.cursor()
    #     c.execute("""
    #         SELECT id, name, count_sent, count_received FROM clinics WHERE id = ?
    #     """, [logistic_id])
    #     return Clinic(*c.fetchone())

    def get_count_received(self, logisric_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT count_received FROM logistics WHERE id = ?
        """, [logisric_id])
        return c.fetchone()[0]

    def update_count_received(self, logistic_id, amount):
        old_amount = self.get_count_received(logistic_id)
        new_amount = old_amount+amount
        c = self._conn.cursor()
        c.execute("""
            UPDATE logistics SET count_received=(?) WHERE id=(?)
        """, [new_amount, logistic_id])

    def get_count_sent(self, logistic_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT count_sent FROM logistics WHERE id = ?
        """, [logistic_id])
        return c.fetchone()[0]

    def update_count_sent(self, logistic_id, amount):
        old_amount = self.get_count_sent(logistic_id)
        new_amount = old_amount+amount
        c = self._conn.cursor()
        c.execute("""
            UPDATE logistics SET count_sent=(?) WHERE id=(?)
        """, [new_amount, logistic_id])
