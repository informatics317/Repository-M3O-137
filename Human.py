from AppData.Local.Programs.Python.Python312.Lib.random import randint
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


class Human:
    hp = BoundedStat('hp', 0, 100)
    mp = BoundedStat('mp', 0, 100)
    def __init__(self, name, age, strength, agility, iq, damage, hp = 100, mp= 100):
        self.name = name
        self.age = age
        self.strength = strength
        self.agility = agility
        self.iq = iq
        self.damage = damage
        self.hp = hp
        self.mp = mp

    def take_damage(self, damage):
        self.hp -= damage

    def regenerate(self, regen):
        self.hp += regen

    @property
    def is_alive(self):
        if self.hp > 0:
            return 1
        else:
            print(f'{self.name} умер')
            return 0


class King(Human):
    def __init__(self, name, age, damage, strength, agility, iq, hp = 100, mp= 100, Excalibur_strike = 35):
        super().__init__(name, age, strength, agility, iq, damage, hp = 100, mp= 100)
        self.Excalibur_strike = Excalibur_strike

    def attack_Excalibur(self, target):
        if self.mp >= 46:
            temp = self.damage + self.Excalibur_strike
            temp_random = randint(1, temp)
            self.mp -= 46
            target.take_damage(temp_random)
            print(f'{self.name} атакует {target.name} мечом, damage = {temp_random}, {target.name} hp = {target.hp}')
        elif self.mp < 46:
            print(f'{self.name} не хватает маны')
            temp = self.damage + int(self.strength * 0.2) + int(self.iq * 0.1)
            temp_random = randint(1, temp)
            target.take_damage(temp_random)
            print(f'{self.name} атакует {target.name}, damage = {temp_random}, {target.name} hp = {target.hp}')

    def take_damage(self, damage):
        if damage < 35:
            self.hp += self.hp - damage + int(damage*0.5)
            self.mp += self.mp - damage + int(damage*0.6)
        else:
            self.hp -= damage


class Mag(Human):
    def __init__(self, name, age, damage, strength, agility, iq, hp = 100, mp= 100, fire_power = 20, healing = 15):
        super().__init__(name, age, strength, agility, iq, damage, hp = 100, mp= 100)
        self.fire_power = fire_power
        self.healing = healing

    def attack_fire(self, target):
        if self.mp >= 43:
            temp = self.damage + self.fire_power
            temp_random = randint(1, temp)
            self.mp -= 43
            target.take_damage(temp_random)
            print(f'{self.name} атакует {target.name} огнем, damage = {temp_random}, {target.name} hp = {target.hp}')
        elif self.mp < 43:
            print(f'{self.name} не хватает маны')
            temp = self.damage + int(self.strength * 0.2) + int(self.iq * 0.3) + int(self.agility * 0.1)
            temp_random = randint(1, temp)
            target.take_damage(temp_random)
            print(f'{self.name} атакует {target.name}, damage = {temp_random}, {target.name} hp = {target.hp}')

    def take_damage(self, damage):
        if damage <= 55:
            self.hp = self.hp - damage + int(damage * 0.8)
            self.mp += self.mp - damage + int(damage * 0.6)
        else:
            self.hp -= damage

    def heal(self, target):
        if self.mp >= 10:
            print(f'{self.name} лечит {target.name}')
            temp = self.healing + int(self.iq*0.4)
            self.mp -= 10
            target.regenerate(temp)
        elif self.mp < 10:
            print(f'{self.name} не хватает маны для лечения')


class Knight(Human):
    def __init__(self, name, age, damage, strength, agility, iq, hp = 100, mp= 100, shield = 100, spear_power = 25):
        super().__init__(name, age, strength, agility, iq, damage, hp = 100, mp= 100)
        self.shield = shield
        self.spear_power = spear_power


    def attack_spear(self, target):
        if self.mp >= 50:
            temp = self.damage + self.spear_power + int(self.strength*0.5)
            temp_random = randint(1, temp)
            self.mp -= 50
            target.take_damage(temp_random)
            print(f'{self.name} атакует {target.name} копьем, damage = {temp_random}, {target.name} hp = {target.hp}')
        elif self.mp < 50:
            print(f'{self.name} не хватает маны')
            temp = self.damage + int(self.strength * 0.3) + int(self.iq * 0.2) + int(self.agility * 0.2)
            temp_random = randint(1, temp)
            target.take_damage(temp_random)
            print(f'{self.name} атакует {target.name}, damage = {temp_random}, {target.name} hp = {target.hp}')

    def take_damage(self, damage):
        if self.shield > 0 and self.shield > damage:
            self.shield -= damage
            print(f'{self.name} использовал щит', 'Щит =', self.shield)
        else:
            self.hp -= damage




king = King('Артур', 45, damage = 24, strength = 25, agility = 15, iq = 109)
mag = Mag('Мерлин', 300, damage = 18, strength = 10, agility = 12, iq = 130)
knight = Knight('Ланселот', 29, damage = 27, strength = 18, agility = 20, iq = 98)




