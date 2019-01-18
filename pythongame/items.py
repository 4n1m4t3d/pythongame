class item:
    def __init__(self, name, description, value, texture):
        self.name = name
        self.description = description
        self.value = value
        self.texture = pygame.load.image(os.path.join('C:/Users/Erik/pythgen/pythongame/images',texture))

class goldcoin(item):
    def __init__(self, amt):
        super().__init__(name= 'Gold Coin', description = 'A coin with {} stamped on it'.format(str(self.amt)), value= self.amt, texture='goldcoin.png')
        self.amt = amt

class weapon(item):
    def __init__(self, name, description, value, damage, texture):
        super().__init__(name, description, value, texture)
        self.damage = damage

class dagger(weapon):
    def __init__(self):
        super().__init__(name= 'Dagger', description= 'An ordinary dagger', value= 5, damage= 10, texture= 'dagger.png')

class godweapon(weapon):
    def __init__(self):
        super().__init__(name= 'God Sword', description= 'A sword once forged by a God', value = 0, damage= 99999999, texture='godweapon.png')
