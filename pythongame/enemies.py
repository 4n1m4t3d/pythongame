class enemy:
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp

    def alive(self):
        return self.hp > 0

class ogre(enemy):
    def __init__(self):
        super().__init__(name = 'Ogre', hp = 30, damage = 15)
