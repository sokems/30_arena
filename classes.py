

class Thing:
    """
    Класс содержит в себе следующие параметры:
    - название (name);
    - процент защиты (percent_defense);
    - атаку (attack);
    - жизнь (hp);

    Это могут быть предметы одежды,
    магические кольца, всё что угодно)
    """

    def __init__(self, name, percent_defense, attack_damage, hp):
        self.name = name
        self.percent_defense = percent_defense
        self.attack_damage = attack_damage
        self.hp = hp

    def __str__(self):
        return self.name


class Person:
    """
    Класс, содержащий в себе следующие параметры:
    - Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты;
    - Метод, принимающий на вход список вещей equip_things(things);
    - Метод вычитания жизни на основе входной атаки take_damage(attack_damage);
    """

    def __init__(self, name, percent_defense, attack_damage, hp):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage
        self.percent_defense = percent_defense

    def equip_things(self, things):
        """Метод принимает на вход список вещей и меняет базовые параметры"""
        for thing in things:
            self.hp += thing.hp
            self.percent_defense += thing.percent_defense
            self.attack_damage += thing.attack_damage

    def take_damage(self, attack_damage):
        """Метод принимает на вход наносимый урон и вычитает жизни"""
        damage = attack_damage - attack_damage * self.percent_defense
        self.hp -= damage

    def __str__(self):
        return self.name


class Paladin(Person):
    """
    Класс наследуется от персонажа,
    при этом количество присвоенных жизней и процент защиты умножается на 2;
    """

    def __init__(self, name, percent_defense, attack_damage, hp):
        super().__init__(name, percent_defense, attack_damage, hp)
        self.hp *= 2
        self.percent_defense *= 2


class Warrior(Person):
    """
    Класс наследуется от персонажа,
    при этом атака умножается на 2.
    """

    def __init__(self, name, percent_defense, attack_damage, hp):
        super().__init__(name, percent_defense, attack_damage, hp)
        self.attack_damage *= 2


class Elf(Person):
    """
    Класс наследуется от персонажа,
    при этом атака делится на 2,
    количество присвоенных жизней умножаются на 3.
    """

    def __init__(self, name, percent_defense, attack_damage, hp):
        super().__init__(name, percent_defense, attack_damage, hp)
        self.attack_damage /= 2
        self.hp *= 3
