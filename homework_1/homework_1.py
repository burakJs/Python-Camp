simpleStr = 'Burak' # Metinsel Ifade
simpleFloat = 10.5 # Ondalıklı ifade
simpleInt = 10 # Tam Sayı 
simpleBool = True # Mantıksal Ifade
simpleList = [1, 2, 3] # Liste

# Değişken Tip Örnekleri
programs = ['Ders Programi', 'Degerlendirme', 'Odev-1', 'Odev-2']
isLoggedIn = True
isCompletedProgram = False
completePercentage = 69
isJoinedToCourse = False

def navigate(page):
  print(f'navigated to {page}')

def showAuthBar(isLoggedIn):
  print(f'Auth Bar visible : {isLoggedIn}')

# Eğer programa dahil ise program detay sayfası değilse katılma sayfasına gitme
if isJoinedToCourse:
  navigate('Course_Detail')    
else:
  navigate('Course_Join')

# Giriş yapılı veya değilse üstteki barda gözüküceklerin değişmesi
if isLoggedIn: 
  showAuthBar(True)
else: 
  showAuthBar(False)

