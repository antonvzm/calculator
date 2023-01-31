# Функции исключений
import logging
from user_interface import menu


def div_zero(li):
    num = li[1]
    while True:
        if num == 0:
                logging.error("error: division by zero")
                print("Ошибка: на 0 делить нельзя, введите корректные данные")
                num = int(input("Введите второе число: "))
        else:
            break
    new_li = [li[0], num]
    return new_li


def operation_vert(num):
    if num < 6 and num > 0: 
        return num
    elif num == 6:
        logging.info("return to job selection")
        print("Возврат в главное меню")
        menu()
    else:
        while True:
            if num < 1 or num > 6:
                logging.error("error: Input Error operation")
                print("Ошибка: введите корректные данные")
                num = int(input("Выберите операцию: \n"
                            "1 - +\n"
                            "2 - -\n"
                            "3 - *\n"
                            "4 - /\n"
                            "5 - **\n"
                            "6 - вернуться в предыдущее меню \n"
                            ))
            return num
