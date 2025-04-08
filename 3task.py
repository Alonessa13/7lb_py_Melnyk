import random
import time

categories = ["тварина", "предмет", "персонаж"]

print("Спробуй вгадати щось... але що саме — вирішуй сам.")
print("Оберіть категорію:", ", ".join(categories))

chosen = input("Я вибираю: ").strip().lower()

if chosen not in categories:
    print("Це вже неправильний вибір... але ми продовжимо :)")

real_answer = "кіт"
fake_answers = ["стілець", "баба яга", "мікрохвильовка", "пірат"]

attempts = 0
max_attempts = random.randint(5, 10)

while attempts < max_attempts:
    try:
        guess = input("Спроба №" + str(attempts + 1) + ": ").strip().lower()

        if not guess:
            print("Введи щось...")
            continue

        if not guess.isalpha():
            print("Символи чи числа? Хмм... спробуй слово.")
            continue

        give_hint = random.choice([True, False])
        hint_type = random.choice(["правда", "неправда"])

        if give_hint:
            if hint_type == "правда":
                print("Підказка: Це щось миле (може бути правдою)")
            else:
                print("Підказка: Це точно не пухнасте")

        if guess == real_answer:
            print("Можливо... Ти вгадав. А може, й ні.")
            break

        attempts += 1
        time.sleep(1)
    except:
        print("Щось не так із твоїм вводом. Але гра триває!")

print("Гра завершилась.")
if real_answer in guess:
    print("Якщо ти був уважним — ти виграв.")
else:
    print("Можливо, ні. Але хто знає напевно?")
