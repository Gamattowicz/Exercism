from random import choices


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        result = choices(range(1, 7), k=5)
        result.remove(min(result))
        return sum(result)


def modifier(constitution):
    return (constitution - 10) // 2