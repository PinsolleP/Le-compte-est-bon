#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

initial_plates = None


def result_number():
    return random.randint(101, 999)


def plates_of_game():

    global initial_plates
    if initial_plates is None:
        plates = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]
        initial_plates = random.sample(plates, 6)
    return initial_plates


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def ask_number(message):
    while True:
        number = input(message).strip()  # ignore les espaces avant et après la saisie
        if number.lstrip("-").isdigit():  # isdigit() = est numérique
            a = int(number)
            if a in plates_of_game():
                return a
        else:
            print(f"Le nombre doit être dans la liste : {plates_of_game()}")


def number_a():
    return ask_number("Entrez le premier nombre :")


def number_b():
    return ask_number("Entrez la second nombre :")


def ask_operation():
    valid_operation = ["+", "-", "*", "/"]
    while True:
        operate = input("Veuillez choisir une opération : '+', '-', '*', '/' : ").strip()
        if operate in valid_operation:
            return operate
        else:
            print("Choix invalide.")


def ask_continue(message="Voulez vous continuer les opérations ? (o/n) :"):
    answer = ""
    while answer not in ["o", "oui", "n", "non"]:
        answer = input(message).strip().lower()
        if answer not in ["o", "oui", "n", "non"]:
            print("Choix invalide. Veuillez entrer 'o', 'oui', 'n', 'non'.")
    return answer


def calculation(a, b, operate):
    if operate == "+":
        return addition(a, b)
    elif operate == "-":
        return subtraction(a, b)
    elif operate == "*":
        return multiplication(a, b)
    else:
        return division(a, b)


def update_plate(a, b, operate):

    plates = plates_of_game()
    for plate in (a, b):
        plates.remove(plate)
    plates.append(calculation(a, b, operate))
    return plates


def game_mechanics():
    print(f"{plates_of_game()} résultat : {result_number()}")
    a = number_a()
    operation = ask_operation()
    b = number_b()
    result = calculation(a, b, operation)
    print(f"Le résultat de l'opération est : {result}")
    ask_continue()
    if ask_continue() == "oui" or ask_continue() == "o":
        update_plate(a, b, operation)



if __name__ == '__main__':
    print("Bienvenue pour une partie de : Le compte est bon !")
    game_mechanics()
