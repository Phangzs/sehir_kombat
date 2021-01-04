import time
import random
from colorama import Fore, Back, Style

heroName1 = str
heroHealth1 = 100

heroName2 = str
heroHealth2 = 100

hero1First = bool
isGameOver = False


def firstHero():
    print("--- First Hero ---")
    global heroName1
    heroName1 = Fore.RED + input("Please type your hero's name: ") + Style.RESET_ALL
    if heroName1.replace(" ", "") == "":
        print("Please enter a valid name!\n\n")
        time.sleep(1)
        firstHero()


def secondHero():
    print("\n\n--- Second Hero ---")
    global heroName2
    heroName2 = Fore.LIGHTBLUE_EX + input("Please type your hero's name: ") + Style.RESET_ALL
    if heroName2.replace(" ", "") == "":
        print("Please enter a valid name!\n\n")
        time.sleep(1)
        secondHero()
    elif heroName2 == heroName1:
        print(f"{heroName1} is already taken, please choose another name!")
        time.sleep(1)
        secondHero()


def firstPlayer():
    global hero1First
    firstPlayer = random.randint(1, 2)
    if firstPlayer == 1:
        print(f"\n\n{heroName1} goes first!\n\n")
        hero1First = True
    else:
        print(f"{heroName2} goes first!")
        hero1First = False


def attackMagnitude(name):
    attackMagnitudeNumber = input(f"{name} attack magnitude (1-50): ")
    try:
        attackMagnitudeNumber = int(attackMagnitudeNumber)
    except ValueError:
        print("Please enter a number")
        attackMagnitudeNumber = attackMagnitude(name)
    if 1 <= attackMagnitudeNumber <= 50:
        return attackMagnitudeNumber
    elif attackMagnitudeNumber == 0:
        print("Why would you do that. Stop.\n")
        attackMagnitudeNumber = attackMagnitude(name)
        return attackMagnitudeNumber
    else:
        print("Attack magnitude must be between 1 and 50!\n")
        attackMagnitudeNumber = attackMagnitude(name)
        return attackMagnitudeNumber


def fight():
    global heroName1
    global heroName2
    global heroHealth1
    global heroHealth2
    global isGameOver
    global hero1First

    if heroHealth1 <= 0 or heroHealth2 <= 0:
        isGameOver = True
        return
    else:
        nameLength1 = len(heroName1) - 6 + len(str(heroHealth1))
        nameLength2 = len(heroName2) - 6 + len(str(heroHealth2))

        if nameLength1 > 12:
            heroName1 = heroName1[:nameLength1 - (nameLength1 - 10)]
            heroName1 += "..."
            print(f"{heroName1}:[{heroHealth1}HP]", end=" " * 9)
        else:
            print("hi")
            print(f"{heroName1}:[{heroHealth1}HP]", end=" " * (23 - nameLength1))

        if nameLength2 > 12:
            heroName2 = heroName2[:nameLength2 - (nameLength2 - 10)]
            heroName2 += "..."
            print(f"{heroName2}:[{heroHealth2}HP]")
        else:
            print(f"{heroName2}:[{heroHealth2}HP]")

        print(Fore.GREEN + "|" * int(heroHealth1 / 5) + Style.RESET_ALL, end="")
        print(Fore.RED + "|" * int((100 - heroHealth1) / 5) + Style.RESET_ALL, end=" " * 5)

        print(Fore.GREEN + "|" * int(heroHealth2 / 5) + Style.RESET_ALL, end="")
        print(Fore.RED + "|" * int((100 - heroHealth2) / 5) + Style.RESET_ALL)

        # ||||||

    if hero1First:
        hero1First = False
        heroAttack1 = attackMagnitude(heroName1)
        dice = random.randint(0, 100)
        if (100 - heroAttack1) > dice:
            print(f"{heroName1} sucessfully hits {heroName2} for {heroAttack1} damage!")
            if heroHealth2 - heroAttack1 < 0:
                heroHealth2 = 0
            else:
                heroHealth2 -= heroAttack1
            print(f"{heroName2} now has {heroHealth2} hitpoints left.")
        else:
            print(f"{heroName1} missed their hit and dealt 0 damage.")
            print(f"{heroName2} now has {heroHealth2} hitpoints left.")
    else:
        hero1First = True
        heroAttack2 = attackMagnitude(heroName2)
        dice = random.randint(0, 100)
        if (100 - heroAttack2) > dice:
            print(f"{heroName2} sucessfully hits {heroName1} for {heroAttack2} damage!")
            if heroHealth1 - heroAttack2 < 0:
                heroHealth2 = 0
            else:
                heroHealth1 -= heroAttack2
            print(f"{heroName1} now has {heroHealth1} hitpoints left.")
        else:
            print(f"{heroName2} missed their hit and dealt 0 damage.")
            print(f"{heroName2} now has {heroHealth2} hitpoints left.")
    print("\n")


def playAgainPrompt2():
    global heroName1
    global heroName2
    global heroHealth1
    global heroHealth2
    global isGameOver
    heroHealth1 = 100
    heroHealth2 = 100
    isGameOver = False
    sameHeroes = input("Same heroes?(y/n)\n").lower()
    if sameHeroes == "y":
        while not isGameOver:
            fight()
        else:
            gameOver()
    elif sameHeroes == "n":
        play()
    else:
        print("Please enter a valid answer!\n")
        playAgainPrompt2()


def playAgainPrompt1():
    playAgain = input("Would you like to play again?(y/n)\n").lower()
    if playAgain == "y":
        playAgainPrompt2()
    elif playAgain == "n":
        print("\nTHANKS FOR PLAYING!\nSEHIR KOMBAT\nBy: Erik and Ethan")
    else:
        print("Please enter a valid answer!\n")
        playAgainPrompt1()


def gameOver():
    global heroName1
    global heroName2
    global heroHealth1
    global heroHealth2
    global isGameOver
    line = "|"
    print("\nGame Over!")
    if heroHealth1 == 0:
        print(f" {line * 30} {heroName2} has won the fight! {line * 30}")
    else:
        print(f" {line * 30} {heroName1} has won the fight! {line * 30}")
    playAgainPrompt1()


def play():
    firstHero()
    secondHero()
    firstPlayer()
    while not isGameOver:
        fight()
    else:
        gameOver()


play()