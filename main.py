from abc import ABC, abstractmethod

# Абстрактный класс оружия
class Weapon(ABC):
    def __init__(self, damage):
        self.damage = damage

    @abstractmethod
    def attack(self):
        pass

# Класс меча
class Sword(Weapon):
    def __init__(self, damage=15):
        super().__init__(damage)

    def attack(self):
        return f"наносит удар мечом, нанося {self.damage} урона."

# Класс лука
class Bow(Weapon):
    def __init__(self, damage=10):
        super().__init__(damage)

    def attack(self):
        return f"наносит удар из лука, нанося {self.damage} урона."

# Абстрактный класс существа
class Creature(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self):
        pass

# Класс бойца
class Fighter(Creature):
    def __init__(self, name, health, weapon: Weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self):
        return f"{self.name} {self.weapon.attack()}"

# Класс монстра
class Monster(Creature):
    def __init__(self, name, health, weapon: Weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        return f"{self.name} {self.weapon.attack()}"

# Механизм боя
def battle(fighter: Fighter, monster: Monster):
    print(fighter.attack())
    monster.health -= fighter.weapon.damage
    if monster.health <= 0:
        print(f"{monster.name} побежден!")
        return
    print(monster.attack())
    fighter.health -= monster.weapon.damage
    if fighter.health <= 0:
        print(f"{fighter.name} побежден!")
    else:
        print(f"У {fighter.name} осталось {fighter.health} здоровья. У {monster.name} осталось {monster.health} здоровья.")

# Демонстрация
sword = Sword()
bow = Bow()
attacker = Fighter("Рыцарь", 100, sword)
defender = Monster("Орк", 80, bow)

battle(attacker, defender)