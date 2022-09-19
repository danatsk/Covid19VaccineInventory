import sqlite3
import DBparser as parser
import sys
import Orders

con = sqlite3.connect('database.db')


# Main function
def main(*args):
    # file = open('config.txt')
    parser.parse(sys.argv[1])
    orders = Orders.Orders()
    orders.execute_orders(sys.argv[2], sys.argv[3])


# Main call
if __name__ == '__main__':
    main(sys.argv)
