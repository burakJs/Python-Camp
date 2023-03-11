# functions

price = 100
discount = 20

# definition define
def calculate():
  print(100 - 20)

def calculateWithParams(price, discount):
  print(price - discount)

def sayHello(name):
  print(f'Hello {name}')

calculate()

calculateWithParams(50, 10)
calculateWithParams(100, 30)

sayHello('Burak')
sayHello('Halit')
sayHello('Mevlüt')

def calculateAndReturn(price, discount):
  return price - discount

newPrice = calculateAndReturn(200, 50)
print(newPrice + 10)

def calculatePrice(price, discount):
  print(price - discount)

def calculatePriceAndReturn(price, discount):
  return price - discount

print('***************')

func1 = calculatePrice(100, 50)
func2 = calculatePriceAndReturn(300, 100)
print(f'41. line: {func1 + 100}')
print(f'42. line: {func2 + 100}')

print('***************')
