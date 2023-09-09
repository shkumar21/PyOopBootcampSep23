class Product:
  def __init__(self, name, quant, price):
    self.name = name #attributs
    self.quant = quant
    self.price = price

  def cost(self): #method
    return self.quant*self.price
  def sell(self, nunits):
     self.quant-=nunits
  #inventory = Product(pr_dict['name'], pr_dict['quant'], pr_dict['price'])
  