print("Kodlama IO")
title = "Transport Credit"
print(title)

# string => metinsel ifade
title = "Personal Finance Credit"
print(title)

# int, integer => tam sayı
maturity = 36
additionalMaturity = 6
maturity2 = '36'

# float, decimal, double
monthlyPayment = 200.50

# bool, boolean => True veya False
isRising = False

# matematiksel operatörler
print(5 + 5)
print(maturity + 12)
print(maturity + additionalMaturity)
print(36 + 6)

print('')
print(5 - 5)
print(maturity - 12)
print(maturity - additionalMaturity)
print(36 - 6)

print('')
print(5 * 5)
print(maturity * 12)
print(maturity * additionalMaturity)
print(10 * 10)

print('')
print(5 / 5)
print(maturity / 12)
print(maturity / additionalMaturity)
print(10 / 2)

newMaturity = maturity / 2
price = 100
discountPrice = price - 20

print(newMaturity)
print(discountPrice)

# % => mod operator
print(10 % 2)
print(maturity % 5)
print(maturity & additionalMaturity)
print(30 % 10)

# mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)

print(1 != 1)
print(1 != 2)

# or and 

# or => veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)
print(1 > 2 and 5 > 2 and 3 > 2)

print(1 > 2 and 3 > 2 or 5 > 2)
print(1 > 2 and 3 > 2 or 5 > 2)

# karar yapuları
# if else 
num1 = 10
num2 = 15
# sayi1 say2den büyükse ekrana sayi1 daha büyük yazdır
# condition
print('******************')
# indent
if num1 <= num2:
  print("Sayi 1 sayi 2'den küçüktür")
elif num1 == num2:
  print("Iki sayi birbirine eşittir")
else: 
  print("Sayi 1 sayi 2'den büyüktür")
print("Hala if bloğunun dişidir")
