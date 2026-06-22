# - створити функцію яка обчислює та повертає площу прямокутника зі сторонами а і б
def area_rectangle(a, b):
    return a * b

a = 5
b = 10

print(f'The area of the rectangle with sides {a} and {b} is {area_rectangle(a, b)}')


# - створити функцію яка обчислює та повертає площу кола з радіусом r
def area_circle(r):
    import math
    return math.pi * r ** 2

r = 10

print(f'The area of the circle with radius {r} is {area_circle(r)}')


# - створити функцію яка обчислює та повертає площу циліндру висотою h, та радіутом r
def area_cylinder(h, r):
    import math
    return 2 * math.pi * r * h + 2 * math.pi * r ** 2

h = 10
r = 5

print(f'The area of the cylinder with height {h} and radius {r} is {area_cylinder(h, r)}')


# - створити функцію яка приймає масив та виводить кожен його елемент
def print_array(arr):
    for i in arr:
        print(i)

arr = [1, 5, 10]

print_array(arr)


# - створити функцію sum(arr) яка приймає масив чисел, сумує значення елементів масиву та повертає його. Приклад sum([1,2,10]) //->13
def sum_array(arr):
    result = 0
    for i in arr:
        result += i
    return result

arr = [1, 5, 10]

print(f'The sum of the array {arr} is {sum_array(arr)}')