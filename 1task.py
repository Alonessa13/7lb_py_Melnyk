import random
# Загаданий об'єкт
secret = "дракон"
hints = [
    "Це може літати",
    "Це щось дуже гаряче",
    "Це з казок",
    "Це може бути і зеленим, і червоним"
]
print("Спробуй вгадати, про кого або що йдеться!")
attempts = 0
max_attempts = random.randint(4, 7)
while attempts < max_attempts:
    try:
        guess = input("Твоя версія: ").strip().lower()
        if not guess.isalpha():
            print("Вводь тільки слова без цифр або символів.")
            continue
        attempts += 1
        if guess == secret:
            print("Правильно! Це був дракон. Перемога!")
            break
        else:
            if random.choice([True, False]):
                print("Ні, але підказка: " + random.choice(hints))
            else:
                print("Ні, спробуй ще.")
    except Exception as e:
        print("Щось пішло не так. Спробуй ще раз.")
if attempts == max_attempts:
    print("Гру завершено. Це був дракон!")
