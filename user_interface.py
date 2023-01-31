# Меню калькулятора

import logging

def menu():
    while True:
        type_num = input("Выберете с какими числами будете работать: \n"
                            "1 - с рациональными\n"
                            "2 - с комплексными\n"
                            "3 - закончить работу\n")
        match type_num:
            case "1" | "2":
                menu_calc(type_num)
                break
            case "3":
                logging.info("menu exit")
                print("Конец работы")
                break
            case _:
                logging.error("error: Input Error menu")
                print("Ошибка: введите корректные данные")

def enter_num():
    num = [float(input("Введите первое число: ")), float(input("Введите второе число: "))]
    return num


import mod_calc
import excep

def menu_calc(num):
    if num == "1":
        logging.info("selected operations with rational numbers")
        num_op = excep.operation_vert(int(input("Выберите операцию: \n"
                            "1 - +\n"
                            "2 - -\n"
                            "3 - *\n"
                            "4 - /\n"
                            "5 - **\n"
                            "6 - вернуться в предыдущее меню \n"
                            )))
        match num_op:
            case 1:
                mod_calc.num_sum(enter_num())
            case 2:
                mod_calc.num_diff(enter_num())
            case 3:
                mod_calc.num_mult(enter_num())
            case 4:    
                mod_calc.num_div(excep.div_zero(enter_num()))
            case 5:
                mod_calc.num_degree(enter_num())
    else:
        logging.info("selected operations with complex numbers")
        mod_calc.num_complex_num(enter_num())