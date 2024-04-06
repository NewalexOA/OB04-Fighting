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
    @abstractmethod
    def attack(self):
        pass

# Класс бойца
class Fighter(Creature):
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self):
        return f"Боец {self.name} {self.weapon.attack()}"

# Класс монстра
class Monster(Creature):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return f"Монстр {self.name} атакует!"

# Простой механизм боя
def battle(fighter: Fighter, monster: Monster):
    attack_message = fighter.attack()
    print(attack_message)
    damage = fighter.weapon.damage
    monster.health -= damage
    if monster.health <= 0:
        print(f"{monster.name} побежден!")
    else:
        print(f"У {monster.name} осталось {monster.health} здоровья.")

# Демонстрация
sword = Sword()
bow = Bow()
fighter = Fighter("Артур", sword)
monster = Monster("Горгулья", 30)

# Боец выбирает меч
battle(fighter, monster)

# Боец меняет оружие на лук
fighter.changeWeapon(bow)
# Боец выбирает лук
battle(fighter, monster)
