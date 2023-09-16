class inventory:
    def __init__(self, products):
        self._products = products
        #python convention: _products=>implies this fo internal purpose 
    def total_cost(self):
        return sum(p.cost() for p in self._products)
