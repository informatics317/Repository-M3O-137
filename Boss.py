from Human import*
from random import*

class BoundedStat:
    def __init__ (self, name, min_value=0, max_value=100):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value

    def __set__ (self, instance, value):
        if value < self.min_value:
            value = self.min_value
        elif value > self.max_value:
            value = self.max_value
        instance.__dict__[self.name] = value


class Boss:
    hp = BoundedStat('hp', 0, 550)
    mp = BoundedStat('mp', 0, 150)

    def __init__(self, name, strength, agility, iq, damage, hp = 550, mp = 150):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.iq = iq
        self.damage = damage
        self.hp = hp
        self.mp = mp

    def take_damage(self, damage):
        self.hp -= damage

    def attack(self, target):
        temp = self.damage + self.strength + int(self.agility * 0.3)
        temp_random = randint(1, temp)
        self.mp += 10
        target.take_damage(temp_random)
        print(f'{self.name} атакует {target.name}, damage = {temp_random}, {target.name} hp = {target.hp}')

    def attack_everyone(self, target1, target2, target3):
        self.mp -= 40
        temp_random = randint(1, 20)
        target1.take_damage(temp_random)
        target2.take_damage(temp_random)
        target3.take_damage(temp_random)
        print(f'{self.name} атакует всех, damage = {temp_random}, {target1.name} hp = {target1.hp}, {target2.name} hp = {target2.hp}, {target3.name} hp = {target3.hp}')

    @property
    def is_alive(self):
        if self.hp > 0:
            return 1
        else:
            return 0


def boss_attack():
    b = randint(1, 5)
    if b == 1 and king.is_alive == 1: boss.attack(king)
    elif b == 2 and mag == 1: boss.attack(mag)
    elif b == 3 and knight == 1: boss.attack(knight)
    elif b == 4: boss.attack_everyone(king, mag, knight)
    else:
        boss_attack()

boss = Boss('Мордред', damage = 20, strength = 25, agility = 35, iq = 95)







