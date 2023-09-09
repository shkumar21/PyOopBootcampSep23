from product import Product
class GSTProduct(Product):
    def __init__(self, name, quant, price, tax): ##redefining init
        super().__init__(name, quant, price) ##calling parents __init
        self.tax = tax

    def panic(self):
        self.sell(self.quant)

    def cost(self):
        actual_cost= super().cost()
        return actual_cost + (self.tax*actual_cost/100)

#main start from here
#p = Product('MINT', 100, 490.10)
#gt = GSTProduct('MINT', 100, 490.15)
tgt = GSTProduct('MINT', 100, 490.15, 25)
#print(f'Old price: {p.cost()}')
#print(f'Price with GST:{ gt.cost()}')
print(f'Price with GST:{ tgt.cost()}')

#reuse, redefine, override
