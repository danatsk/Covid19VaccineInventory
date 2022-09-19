import Repository
from Repository import repo
from Vaccine import Vaccine

class Orders(object):
    def __init__(self):
        self.total_sent = 0
        self.total_received = 0

    def execute_orders(self, orders_file, summery_file):
        summery_list = []
        with open(orders_file) as orders:
            for order_line in orders:
                order = order_line.split(',')
                if len(order) == 3:
                    self.execute_recive(order)
                else:
                    # order[1] = order[1][0:-1]
                    self.execute_send(order)
                line = str(repo.get_total_inventory()) + ', ' + str(repo.get_total_demand()) + ', '
                line += str(self.total_received) + ', ' + str(self.total_sent)+'\n'
                summery_list.append(line)
        with open(summery_file, 'w') as summery:
            summery.writelines(summery_list)

    def execute_recive(self, order):
        vac = Vaccine(repo.get_next_vaccine_id(), order[2], repo.get_supplier_id(order[0]), order[1])
        repo.insert_vaccine(vac)
        repo.update_count_received(int(order[1]), order[0])
        self.total_received += int(order[1])

    def execute_send(self, order):
        clinic_location = order[0]
        amount = int(order[1])
        repo.update_clinic_demand(clinic_location, amount)
        repo.update_count_sent(amount, repo.get_clinic_logistic(clinic_location))
        while amount > 0:
            vac = repo.get_earliest_vaccine()
            if amount >= vac.quantity:
                amount = amount - vac.quantity
                repo.remove_vaccines(vac.id)
            else:
                vac_new_quan = vac.quantity-amount
                repo.update_vaccines_quantity(vac.id, vac_new_quan)
                amount = 0
        self.total_sent += int(order[1])
