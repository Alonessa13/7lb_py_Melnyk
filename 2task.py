import random
secret = "ейнштейн"
# Підказки не дуже очевидні
hints = [
    "Його зачіска стала мемом",
    "Він не любив носити шкарпетки",
    "У нього є фото з висунутим язиком",
    "Він не був дуже організованим, але дуже розумним"
]
used_hints = []
print("Спробуй вгадати відому людину.")
print("Я даватиму підказки, але не всі одразу. Пиши одне слово.")
while True:
    try:
        guess = input("Твоя відповідь: ").strip().lower()
        if not guess.isalpha():
            print("Будь ласка, вводь тільки слово без символів або цифр.")
            continue
        if guess == secret:
            if random.choice([True, False]):
                print("Ти... майже вгадав. Але цього разу — поразка! (Жартую, переміг!)")
            else:
                print("Блискуче! Це дійсно був Ейнштейн. Ти виграв!")
            break
        else:
            if len(used_hints) < len(hints) and random.choice([True, False]):
                next_hint = random.choice([h for h in hints if h not in used_hints])
                used_hints.append(next_hint)
                print("Підказка: " + next_hint)
            else:
                responses = [
                    "Хм... ні, ще думай.",
                    "Не зовсім. Але ти близько. Можливо.",
                    "Цікавий варіант, але ні.",
                    "Може інша епоха? Інший стиль? Інша зачіска?"
                ]
                print(random.choice(responses))
    except:
        print("Помилка вводу. Просто введи слово, окей?")
