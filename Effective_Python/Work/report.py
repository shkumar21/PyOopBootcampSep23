'''
    Displays gain or loss of inventory
'''

import csv

#def read_inventory(filename: str) -> list[tuple]:
def read_inventory(filename):
    '''
        Reads a csv file
        Returns a list of tuples [ for each row ]
    '''
    inv = list()
    with open(filename) as FH:
        data = csv.reader(FH)
        headers = next(data)

        for row in data:
            row = (row[0], int(row[1]), float(row[2]))
            inv.append(row)

    return inv
