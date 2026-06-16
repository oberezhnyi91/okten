1
# Робота з булевими значеннями (Booleans)
# Створіть дві змінні, is_sunny (чи сонячно) та is_warm (чи тепло), і присвойте їм булеві значення (True або False).
# Перевірте, чи можна йти гуляти (умова: сонячно і тепло). Виведіть результат.
# Перевірте, чи можна вдягнути футболку (умова: сонячно або тепло). Виведіть результат.

is_sunny = True
is_warm = False

# can_go_walk = is_sunny and is_warm
if is_sunny and is_warm:
    can_go_walk = True
else:
    can_go_walk = False

print(f"Можна йти гуляти: {can_go_walk}")

if is_sunny or is_warm:
    can_wear_tshirt = True
else:
    can_wear_tshirt = False

print(f"Можна вдягнути футболку: {can_wear_tshirt}")


2
# Маємо змінні day яка символізує назву дня тижня (наприклад, "Понеділок", "Субота")
# і за допомогою конструкції match визначає, чи є цей день робочим, вихідним, чи невірною назвою.
# Визначає тип дня тижня (робочий/вихідний) за його назвою.

day = "Monday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Це робочий день.")
    case "Saturday" | "Sunday":
        print("Це вихідний день.")
    case _:
        print("Невірна назва дня.")