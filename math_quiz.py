import random
import operator


def get_number(n=10):
    return random.randint(1, n + 1)


def equation():
    x = get_number(100)
    y = get_number(100)
    operations = {'+': operator.add(x, y),
                  '-': operator.sub(x, y),
                  '*': operator.mul(x, y),
                  '/': operator.floordiv(x, y)}
    choice = random.choice(list(operations.keys()))
    return f'{x} {choice} {y} = {operations[choice]}'


print(equation())
