from random import randint, choice, uniform

from classes import Thing, Warrior, Paladin


THINGS = [
    Thing("Меч Рыцаря", hp=0, percent_defense=0, attack_damage=15),
    Thing("Щит Защитника", hp=10, percent_defense=0.1, attack_damage=0),
    Thing("Шлем Воина", hp=5, percent_defense=0.05, attack_damage=0),
    Thing("Броня Стража", hp=20, percent_defense=0.03, attack_damage=0),
    Thing("Перчатки Удара", hp=0, percent_defense=0, attack_damage=5),
    Thing("Сапоги Скорости", hp=0, percent_defense=0.1, attack_damage=0),
    Thing("Пояс Силы", hp=10, percent_defense=0, attack_damage=10),
    Thing("Амулет Жизни", hp=25, percent_defense=0, attack_damage=0),
    Thing("Кольцо Защиты", hp=0, percent_defense=0.04, attack_damage=0),
    Thing("Лук Снайпера", hp=0, percent_defense=0, attack_damage=12),
]

PERSON_NAMES = [
    "Геральт",
    "Эцио",
    "Лара Крофт",
    "Артемис",
    "Джейсон Вурхиз",
    "Эдвард Кенуэй",
    "Кратос",
    "Элис",
    "Джон Марстон",
    "Тэсс",
    "Ганнибал",
    "Леголас",
    "Арагорн",
    "Джокер",
    "Бэтмен",
    "Соник",
    "Марио",
    "Супермен",
    "Тони Старк",
    "Капитан Америка"
]


def main():
    things = sorted(THINGS, key=lambda thing: thing.percent_defense)
    heroes = []

    for _ in range(10):
        hero_class = choice([Warrior, Paladin])
        hero = hero_class(
            choice(PERSON_NAMES),
            uniform(0, 0.1),
            randint(0, 50),
            100,
        )

        count_things = randint(1, 4)
        hero_things = [choice(things) for _ in range(count_things)]
        hero.equip_things(hero_things)

        heroes.append(hero)

    print("\n--- Бой начинается! ---\n")

    while len(heroes) > 1:
        attacker, defender = choice(heroes), choice(heroes)
        while defender == attacker:
            defender = choice(heroes)

        damage = attacker.attack_damage * (1 - defender.percent_defense)
        defender.take_damage(attacker.attack_damage)

        print(f"{attacker} наносит удар по {defender} на {damage:.2f} урона. "
              f"Осталось HP у {defender}: {defender.hp:.2f}")

        if defender.hp <= 0:
            print(f"{defender} погибает!")
            heroes.remove(defender)

    print(f"\nПобедитель арены: {heroes[0]}!")


if __name__ == '__main__':
    main()
