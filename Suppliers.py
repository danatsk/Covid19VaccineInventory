from Supplier import Supplier


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Supplier):
        self._conn.execute("""
               INSERT INTO suppliers (id, name, logistic) VALUES (?, ?, ?)
           """, [Supplier.id, Supplier.name, Supplier.logistic_id])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name, logistic FROM suppliers WHERE id = ?
        """, [supplier_id])
        return Supplier(*c.fetchone())

    def get_logistic_id(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT logistic FROM suppliers WHERE id = ?
        """, [supplier_id])
        return c.fetchone()[0]

    def get_id(self, supplier_name):
        c = self._conn.cursor()
        c.execute("""
            SELECT id FROM suppliers WHERE name = ?
        """, [supplier_name])
        return c.fetchone()[0]

    def get_logistic(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT logistic FROM suppliers WHERE id = ?
        """, [supplier_id])
        return c.fetchone()[0]

