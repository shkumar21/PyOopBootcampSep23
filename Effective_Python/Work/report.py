'''
    Displays gain or loss of inventory
'''

import csv
import fileparse as fp
from product import Product

def read_prices(filename:str) -> dict:
    '''
        Reads a prices csv file
        Returns a dictionary with value for each product
    '''
    inv_list = fp.parse_csv(filename, types=[str, float], has_headers=False)
    return dict(inv_list)

#def read_inventory(filename: str) -> list[tuple]:
def read_inventory(filename):
    '''
        Reads a csv file
        Returns a list of tuples [ for each row ]
    '''
    
    inv = fp.parse_csv(filename, 
                 select=['name', 'quant', 'price'],
                 types=[str, int, float])

    inventory = [Product(pr_dict['name'], pr_dict['quant'], pr_dict['price'])
                    for pr_dict in inv ]
    return inventory

    # convert inv .. which is a list of dictionaries
    # to a list of Product instances
    # Return that list of Product instances

def make_report(inventory, prices):
    report = list()
    for prod in inventory:
        name = prod.name
        quant = prod.quant
        latest_price = prices.price
        change = latest_price - prod['price']
        report.append( (name, quant, latest_price, change) )

    return report

def print_report(report):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)

    dashes = tuple(['-' * 10] * 4)
    print('%10s %10s %10s %10s' % dashes)

    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)


def inventory_report(inventory_file, prices_file):
    inventory = read_inventory(inventory_file)
    prices = read_prices(prices_file)
    report = make_report(inventory, prices)
    print_report(report)


def main():
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} invfile pricesfile')

    inv_file = sys.argv[1]
    prices_file = sys.argv[2]
    inventory_report(inv_file, prices_file)

# Main starts from here
if __name__ == "__main__":
    main()
