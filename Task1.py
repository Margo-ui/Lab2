class Client:
  def __init__(self, name, surname, patronymic, number):
    self.name = name
    self.surname = surname
    self.patronymic = patronymic
    self.number = number

  def get_cl_data(self):
    return f"Client: {self.name} {self.surname} {self.patronymic} {self.number}"

class Product:
  def __init__(self, productname, price, weight, tax):
    self.productname = productname
    self.price = price
    self.weight = weight
    self.tax = tax

  def  get_pr_data(self):
    return f"Product: {self.productname} {self.price} {self.weight} {self.tax}"

class Order(Client, Product):
  def __init__(self, name, surname, patronymic, number, productname, price, weight, tax):
    Client.__init__(self, name, surname, patronymic, number)
    Product.__init__(self, productname, price, weight, tax)

  def fprice(self):
    self.fullprice = self.price * self.tax
    return f"Order price: {self.fullprice}"
    #return 7

ord = Order('Sheldon', 'Cooper', 'Lee', '+180756789321', 'train', 50, 20, 2)
print(ord.get_cl_data())
print(ord.get_pr_data())
print(ord.fprice())