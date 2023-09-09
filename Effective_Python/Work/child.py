from product import Product
class Myproduct(Product):
    def panic(self):
        self.sell(self.quant)

#main start from here

p = Myproduct('MINT', 100, 490.10)
p.sell(25)
print(p.quant)
p.panic()
print(p.quant)
