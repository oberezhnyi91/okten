# Створіть словник з назвою fruit_stock.
# Додайте до нього три пари "ключ: значення":
# "apple": 10
# "banana": 15
# "orange": 8
# Виведіть на екран весь словник fruit_stock.
# Виведіть на екран кількість яблук, звернувшись до значення за ключем "apple".
# Додайте новий фрукт до словника: "груша" зі значенням 12.
# Змініть кількість banana: встановіть нове значення 20.
# Виведіть на екран оновлений словник fruit_stock.


fruit_stock = {
    "apple": 10,
    "banana": 15,
    "orange": 8
}
print(fruit_stock)

print(fruit_stock['apple'])
fruit_stock['pear'] = 12
print(fruit_stock)
fruit_stock['banana'] = 20
print(fruit_stock)

# Створення та доступ до елементів списку
#
# Створіть список з назвою shopping_list, який містить наступні рядки: "молоко", "хліб", "яйця", "сир".
# Виведіть на екран весь список.
# Виведіть на екран перший елемент списку (той, що має індекс 0)

shopping_list = ["milk", "bread", "eggs", "cheese"]
print(shopping_list)
print(shopping_list[0])

# Створи список із 7 собак.
# Кожна собака — словник з трьома полями: "name" (кличка), "age" (вік), "breed" (порода).
# Виведи третю собаку зі списку та її кличку.

dogs = [
    {"name": "Rex", "age": 5, "breed": "Labrador"},
    {"name": "Bim", "age": 3, "breed": "Husky"},
    {"name": "Tuzik", "age": 4, "breed": "Shepherd"},
    {"name": "Barney", "age": 2, "breed": "Pug"},
    {"name": "Charlie", "age": 6, "breed": "Bulldog"},
    {"name": "Lucky", "age": 1, "breed": "Corgi"},
    {"name": "Max", "age": 7, "breed": "Doberman"}
]
print(dogs[2])
print(dogs[2]['breed'])
print(dogs[2]['name'])