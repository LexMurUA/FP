import random
import math
from functools import lru_cache
import time

def decorating(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()        
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        need_time = end_time - start_time
        print(f"Execution time: {need_time} seconds")
        return result
    return wrapper

#1
@decorating
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n ):
        a, b = b, a + b
    return b

n = 25
print(fibonacci_iterative(n))

#2
@decorating
@lru_cache(maxsize=None)
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n ):
        a, b = b, a + b
    return b
 
n = 25
print(fibonacci_iterative(n))

#3
@decorating
@lru_cache(maxsize=16)
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n ):
        a, b = b, a + b
    return b
 
n = 25
print(f'Кеш-16={fibonacci_iterative(n)}')

#4
@decorating
@lru_cache(maxsize=10)
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n ):
        a, b = b, a + b
    return b
 
n = 25
print(f'Кеш-10={fibonacci_iterative(n)}')







