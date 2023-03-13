students = []

def getFullName(firstName, lastName) -> str:
  return f'{firstName} {lastName}'

def addStudent(firstName, lastName):
  students.append(getFullName(firstName, lastName))

def removeStudent(firstName, lastName):
  searchValue = getFullName(firstName, lastName)
  isFound = False
  
  for i in students: 
    if searchValue == i:
      isFound = True
      students.remove(i)
      break

  if not isFound: print('This student not found')

def addStudentList(studentList):
  if isinstance(studentList, list):
    students.extend(studentList)
  else: 
    print('Please enter correct type parameter')

def showStudent():
  i = 0
  print('\n***** START ******')
  while i < len(students):
    print(students[i])
    i += 1
  print('***** END ******\n')

def getStudentNumber(firstName, lastName) -> int:
  searchValue = getFullName(firstName, lastName)
  isFound = False

  for i in range(len(students)):
    if students[i] == searchValue:
      isFound = True
      return i

  if not isFound: 
    print('This student not found')
    return -1

def removeStudentFromNumber(studentNumbers):
  if isinstance(studentNumbers, list):
    studentNumbers.sort(reverse = True)
    for i in studentNumbers:
      if not isinstance(i, int) or i > len(students) - 1: 
        print('Please enter correct number list')
        return
      students.pop(i)
  else:
    print('Please enter correct type parameter')

addStudent('Burak', 'Imdat')
showStudent()
addStudentList('X')
addStudentList(['Burak2 Imdat2', 'Burak3 Imdat3'])
showStudent()
removeStudent('Burak2', 'Imdat2')
showStudent()
print(f'Student Number: {getStudentNumber("Burak", "Imdat")}')
removeStudentFromNumber(1)
showStudent()
removeStudentFromNumber([5])
showStudent()
removeStudentFromNumber([0, 1])
showStudent()
