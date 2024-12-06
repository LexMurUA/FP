# Напишіть декоратор, який буде заміряти час виконання для наданої функції.
import time
from operator import neg, mul, le
from functools import reduce, partial

def decorating(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()        
        result = func(*args, **kwargs)
        end_time = time.time()
        need_time = end_time - start_time
        print(f"Execution time: {need_time} seconds")
        return result
    return wrapper

ssd = [1,2,3,4,5,5]
@decorating
def negatives(value):
    return list(map(neg, range(value)))

print(f'Негатив-{negatives(5000)}')

@decorating
def reduce_mod(value):
    return reduce(mul, value)

print(f'добуток-{reduce_mod(ssd)}')

@decorating
def prti(value):
    return list(filter(partial(le, 5)))

print(f'Числа менше 5-{prti[1,2,3,4,5,5]}')
