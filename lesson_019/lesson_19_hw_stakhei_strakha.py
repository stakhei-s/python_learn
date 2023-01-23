import random
import math
import logging

'''
Напишите декоратор debug, который при каждом вызове 
декорируемой функции выводит её имя (вместе со всеми 
передаваемыми аргументами), а затем — какое значение 
она возвращает. После этого выводится результат её 
выполнения

'''
lst_a_b_c = []
lst_i = []
for i in range(20):
    lst_i.append(random.randint(1, 20))
    lst_i.append(random.randint(1, 20))
    lst_i.append(random.randint(1, 20))
    lst_a_b_c.append(lst_i)
    lst_i = []

print(lst_a_b_c)

logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    filemode='w',
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s - %(levelno)s",
    datefmt='%H:%M:%S',
)

logging.info('start')


def decorator(func):
    def wapper(a, b, c):
        print(f'Функция - {func.__name__}, принимает аргументы: {a}, {b} и {c}, результат функции {func(a, b, c)}')
        # print(func(a,b,c))

    return wapper


@decorator
def roots_of_the_quadratic_equation(a, b, c):
    discr = b ** 2 - 4 * a * c

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        logging.debug(f'{a=} {b=} {c=} ok')
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        logging.info(f'{a=} {b=} {c=} one solution')
        return x
    else:
        logging.warning(f"{a=} {b=} {c=} don't solution")
        return 'N/A'


for i in lst_a_b_c:
    roots_of_the_quadratic_equation(i[0], i[1], i[2])

logging.info('finish')