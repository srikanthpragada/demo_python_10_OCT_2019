# superclass
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

    def get_price(self):
        return self.price

# subclass
class DiscountProduct(Product):
    def __init__(self,name,price,disrate):
        Product.__init__(self,name,price)
        # super().__init__(name,price)
        self.disrate = disrate

    def __str__(self):
        return super().__str__() + " - " + str(self.disrate)

    def get_price(self):
        return self.price - self.price * self.disrate / 100

    def set_disrate(self,newdisrate):
        if newdisrate < 5 or newdisrate > 50:
            raise ValueError("Invalid Discount Rate")

        self.disrate = newdisrate


p = Product("Dell Laptop",50000)
print(p)
dp = DiscountProduct("HP Laptop",60000,20)
print(dp)

print(p.get_price(), dp.get_price())