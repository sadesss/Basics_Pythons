# Напишите функцию phib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
# В этой задаче нельзя использовать циклы - используйте рекурсию.

n = int(input())



def phib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return phib(n - 1) + phib(n - 2)


print(phib(n))
