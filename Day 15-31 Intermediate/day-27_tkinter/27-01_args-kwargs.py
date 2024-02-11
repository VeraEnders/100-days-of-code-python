def add(*args):
  for n in args:
    print(n)

add(4, 8, 6, 7)

def calculate(n, **kwargs):
  print(kwargs)
  for key, value in kwargs.items():
    print(key)
    print(value)

  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)

calculate(2, add=3, multiply=5)

class Car:

  def __init__(self, **kw):
    self.make = kw.get("make")
    self.model = kw.get("model")
    self.color = kw.get("color")
    self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Model")
print(my_car.model)