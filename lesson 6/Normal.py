# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person:
    def __init__(self, name):
        self._name = name
        self._health = 100.0
        self._damage = 15.0
        self._armor = 100.0

    def get_name(self):
        return self.name

    def get_heals(self):
        return self._health

    def set_heals(self, health):
        self._health = health

    def get_damage(self):
        return self._damage

    def set_damage(self, damage):
        self._damage = damage

    def get_armor(self):
        return self._armor

    def set_armor(self, armor):
        self._armor = armor

    def taking_damage(self, damage):
        if self._armor > 0:
            percent_armor_damage = float(random.randint(0, 100) / 100)
            self._armor -= float(damage * percent_armor_damage)
            self._health -= float(damage * (1.0 - percent_armor_damage))
            if self._armor < 0:
                self._armor = 0
            if self._health < 0:
                self._health = 0
            print('У {} осталось здоровья - {}, брони - {}'.format(self._name, int(self._health), int(self._armor)))
        else:
            self._health -= damage
            if self._health < 0:
                self._health = 0
            print('У {} осталось здоровья - {}'.format(self._name, int(self._health)))


class Enemy(Person):
    def __init__(self, name):
        super().__init__(name)
        self.set_heals(150)
        self.set_damage(10)


class Player(Person):
    def __init__(self, name):
        super().__init__(name)
        self.set_damage(20)


player = Player('Игрок')
enemy = Enemy('Враг')

last_attack_person = 'enemy'
while player.get_heals() > 0 and enemy.get_heals() > 0:
    if last_attack_person == 'enemy':
        enemy.taking_damage(player.get_damage())
        last_attack_person = 'player'
    else:
        player.taking_damage(enemy.get_damage())
        last_attack_person = 'enemy'
