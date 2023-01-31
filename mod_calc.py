# Все действия калькулятора

import logging
from excep import div_zero
from user_interface import menu

def num_sum(a):
    logging.info('addition selected')
    print(f"{a[0]} + {a[1]} = {a[0] + a[1]}")
    menu()

def num_diff(a):
    logging.info('subtraction selected')
    print(f"{a[0]} - {a[1]} = {a[0] - a[1]}")
    menu()

def num_mult(a):
    logging.info('multiplication selected')
    print(f"{a[0]} * {a[1]} = {a[0] * a[1]}")
    menu()

def num_div(a):
    div_zero(a)
    logging.info('division selected')
    print(f"{a[0]} / {a[1]} = {a[0] / a[1]}")
    menu()

def num_complex_num(a):
    logging.info('selected complex numbers')
    print(complex(a[0], a[1]))
    menu()

def num_degree(a):
    logging.info('chosen exponentiation to the second power')
    print(f"{a[0]} ** {a[1]} = {a[0] ** a[1]}")
    menu()

