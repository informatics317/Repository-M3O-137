from Human import*
from Boss import*

print('Игра началась')
print('Персонажи:')
print(king.__dict__)
print(mag.__dict__)
print(knight.__dict__)
print('Ваш противник:')
print(boss.__dict__)

n = 0
while boss.is_alive == 1:
    if king == 0 and mag == 0 and knight == 0:
        print('Увы. Вы проиграли')
        break
    n += 1
    print(f'Раунд {n}')
    if king.is_alive == 1:
        king.attack_Excalibur(boss)
    if mag.is_alive == 1:
        if mag.mp >= 20 and (king.hp < 70 or knight.hp < 70):
            mag.heal(king)
            mag.heal(knight)
        mag.attack_fire(boss)
    if knight.is_alive == 1:
        knight.attack_spear(boss)
    if boss.is_alive == 1:
        boss_attack()
    if boss.is_alive == 0:
        break
print('Мордред мертв')
print('Победа!!!')




