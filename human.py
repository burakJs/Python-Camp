class Human:
  name: str

  def __init__(self, name):
    self.name = name
    print('Human instance was created...')

  def __str__(self) -> str:
    return f'Human with name: {self.name}'
  def talk(self, sentence):
    print(f'{self.name}: {sentence}')

  def walk(self):
    print(f'{self.name} is walking...')
