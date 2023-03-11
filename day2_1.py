# list
# loop

array = ['Personel Finance Credit', 10, 5.2, True]
print(array)

credits = ['Personel Finance Credit', 'Car Loan', 'Housing Loan']
print(type(credits))

print(credits)
print(credits[0])

print(len(credits)) # length
# print(credits[3]) => error

credits.append('Custom Credit')
print(credits)

credits.append('X Credit')
print(credits)

credits.pop(0)
print(credits)

credits.append('Car Loan')
print(credits)
credits.remove('Car Loan')
print(credits)

credits.extend(['Y Credit', 'Z Credit'])
print(credits)


# for 
# i=0 i<10

for i in range(10):
  print('XX')
  print(i)

print('********************')

for i in range(5, 11):
  print(i)

print('********************')

for i in range(0, 51, 10):
  print(i)
  
print('********************')

# for i in range(0.1, 0.5): => ERROR
#   print(i)

credits = ['Personel Finance Credit', 'Car Loan', 'Housing Loan']

for credit in credits:
  print(credit)

print('********************')

for i in range(len(credits)):
  print(credits[i])

print('**************')

# infinity loop

i = 0
while i < 10: 
  print('X')
  i += 1
print('Y')

print('**************')

while True:
  print('X')
  break

print('******* Last Loop *******')

credits = ['Personel Finance Credit', 'Car Loan', 'Housing Loan']

i = 0
while i < len(credits):
  print(i)
  print(credits[i])
  i += 1
  if credits[i] == 'Housing Loan':
    break
