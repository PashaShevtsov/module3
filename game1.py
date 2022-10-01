from exceptions import *
from models import Enemy, Player
import settings
import sys


def enter_name():
    while True:
        name = input("Enter your name: \n")
        if name == "":
            print("You cannot enter an empty line!")
        else:
            break
    return name


def play(name):
    print(
        '\nWIZARD [1]'
        '\nWARRIOR[2]'
        '\nROBBER [3]'
    )
    player = Player(name)
    level = settings.PLAYER_LEVEL
    enemy = Enemy(level)
    while True:
        try:
            print(player.attack(enemy))
            print(player.defence(enemy))
        except EnemyDown:
            print('\nEnemy defeated, next enemy!\n')
            level += 1
            enemy = Enemy(level)
            settings.SCORE += 5
            print(name, ' Lives - ', player.lives)
            print('Enemy level - ', enemy.get_info(), '\n')
            continue


def game(user_name):
    try:
        play(user_name)
    except GameOver:
        print('Game over')
        print('Score :', settings.SCORE)
        file = open('score.txt', 'a')
        file.write(f"Name: {user_name}, Scores: {settings.SCORE}" + '\n')
        file.close()
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')


if __name__ == "__main__":
    try:
        user_name = enter_name()
        print('Hello, ', user_name)
        while True:
            print("\nPlease enter the command: start/help/exit")
            user_input = input('\nEnter command please:  \n ')
            if user_input == 'start':
                game(user_name)
            elif user_input == 'exit':
                sys.exit()
            elif user_input == 'help':
                for i in settings.HELP_LIST:
                    print(i)
            else:
                print('\nIncorrect enter command, try again')
    finally:
        print('\nClose the program')