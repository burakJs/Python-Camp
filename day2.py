interest = 1.59
maturity = '36'
creditName = 'Personel Finance Credit'

print(type(interest))
print(type(maturity))
print(type(creditName))

print(int(maturity) + 12)
# print(int(creditName))
interest = str(interest)
print(type(interest))

maturity = int(input('Please enter the maturity you want: '))
print(type(maturity))
maturity += 12

# string interpolation
# Maturity resulting from the maturity you choose

print('Maturity resulting from the maturity you choose: ' + str(maturity))
print('Maturity resulting from the maturity you choose: {maturity}'.format(maturity = maturity))

name = input('Please enter your name : ')
text = 'Hello {name}'.format(name=name)
print(text)

# f-string
text = f'Hello {1+1}'
print(text)

