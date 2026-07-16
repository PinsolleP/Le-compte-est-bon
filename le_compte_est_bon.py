#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def result_number():
    return random.randint(101, 999)


def plates_of_game():
    plates = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]
    return random.sample(plates, 6)


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b



if __name__ == '__main__':

