from random import randint, choice, uniform

from colorama import init, Fore

from classes import Thing, Warrior, Paladin, Elf


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


def create_random_hero(things, available_names):
    """Создание рандомного персонажа с вещами"""
    hero_class = choice([Warrior, Paladin, Elf])
    name = choice(available_names)
    available_names.remove(name)

    hero = hero_class(
        name=name,
        percent_defense=uniform(0, 0.1),
        attack_damage=randint(0, 50),
        hp=100,
    )

    count_things = randint(1, 4)
    hero_things = [choice(things) for _ in range(count_things)]
    hero.equip_things(hero_things)

    return hero

def create_hero_for_player(things):
    """Создание своего персонажа с вещами"""
    while True:
        choice_player = input('Выбери класс:\n'
              f'1. {Fore.RED}Воин\n'
              f'{Fore.RESET}2. {Fore.BLUE}Паладин\n'
              f'{Fore.RESET}3. {Fore.GREEN}Эльф\n')
        if choice_player == '1' or choice_player == 'Воин':
            hero_class = Warrior
            break
        elif choice_player == '2' or choice_player == 'Паладин':
            hero_class = Paladin
            break
        elif choice_player == '3' or choice_player == 'Эльф':
            hero_class = Elf
            break
        else:
            print('Такого класса не существует!')


    name = input('Введите имя персонажа: ')

    hero = hero_class(
        name=name,
        percent_defense=uniform(0, 0.1),
        attack_damage=randint(0, 50),
        hp=100,
    )

    count_things = randint(1, 4)
    hero_things = [choice(things) for _ in range(count_things)]
    hero.equip_things(hero_things)

    print(f'Были присвоены предметы: {Fore.CYAN}{", ".join(str(thing) for thing in hero_things)}')
    input('\nНажмите любую клавишу, чтобы начать бой!')

    return hero


def main():
    init(autoreset=True)
    things = sorted(THINGS, key=lambda thing: thing.percent_defense)
    heroes = [create_hero_for_player(things),]
    available_names = PERSON_NAMES.copy()

    for _ in range(9):
        heroes.append(create_random_hero(things, available_names))

    print(f"\n{Fore.MAGENTA}--- Бой начинается! ---")

    while len(heroes) > 1:
        attacker, defender = choice(heroes), choice(heroes)
        while defender == attacker:
            defender = choice(heroes)

        damage = attacker.attack_damage * (1 - defender.percent_defense)
        defender.take_damage(attacker.attack_damage)

        print(f"\n{Fore.YELLOW}{attacker} {Fore.RESET}наносит удар по "
              f"{Fore.BLUE}{defender} {Fore.RESET}на "
              f"{Fore.RED}{damage:.2f} урона{Fore.RESET}. "
              f"Осталось HP у {Fore.BLUE}{defender}: "
              f"{Fore.GREEN}{defender.hp:.2f}")

        if defender.hp <= 0:
            print(f"{defender} погибает!")
            heroes.remove(defender)

    print(f"\n---------------\nПобедитель арены: {Fore.MAGENTA}{heroes[0]}!")


if __name__ == '__main__':
    main()
