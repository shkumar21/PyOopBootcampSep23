from report import read_inventory

def receipt(filename):
    inv = read_inventory(filename)
    total = 0
    for prod in inv:
        cost = prod[1]*prod[2]
        total = total + cost
    return total

bill_amount = receipt('Data/inventory.csv')
print(f'Your total bill is: {bill_amount}')

