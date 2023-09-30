# mis1
# number = int(input())
# number2 = int(input())
# if number != number2:
# 	print('число 1 не равно числу 2')
# if number > number2:
# 	print('число 1 больше числа 2')

# mis2
# while True:
#     answer = input("Ты любишь Аниме? ")
#     if answer.lower() == "да" or answer.upper() == 'YES':
#         print("Ohayo!")
#         break

# # mis3
# temperature = input("На улице тепло или холодно? ")
# if temperature.lower() == "тепло" or temperature.lower() == "warm":
#     print("Надень футболку.")
# elif temperature.lower() == "холодно" or temperature.lower() == "cold":
#     print("Надень кофту.")
# else:
#     print("Неизвестный ответ. Пожалуйста, введите 'тепло' или 'холодно'.")

# # mis5
# grade = int(input("Введите оценку от 1 до 10: "))
# if 1 <= grade <= 4:
#     print("Плохо")
# elif 5 <= grade <= 8:
#     print("Хорошо")
# elif 9 <= grade <= 10:
#     print("Отлично")
# else:
#     print("Некорректная оценка. Пожалуйста, введите число от 1 до 10.")

# mis6
import random
# Количество дверей и монет
num_doors = 8
num_coins = 5
# Позиция игрока
player_position = 0
# Позиции дверей, монет и врагов
doors = random.sample(range(1, num_doors + 1), num_coins + 1)
coins = random.sample(range(1, num_doors + 1), num_coins)
enemies = random.sample(range(1, num_doors + 1), num_coins)
print("Добро пожаловать в игру Хагги Вагги!")
print("Пиратский квест: Соберите все монеты и избегайте встреч с врагами!")

while True:
    print("\nВы находитесь у двери", player_position)
    print("Выберите действие:")
    print("1. Открыть дверь")
    print("2. Перейти к следующей двери")
    print("3. Выйти из игры")

    choice = input("Введите номер действия: ")

    if choice == "1":
        if player_position in coins:
            print("Вы нашли монету!")
            coins.remove(player_position)
        elif player_position in enemies:
            print("О нет! Вы встретили врага!")
            print("Игра окончена.")
            break
        else:
            print("Здесь ничего нет.")

    elif choice == "2":
        player_position = (player_position + 1) % num_doors

        if player_position == 0:
            print("Вы перешли к следующей двери.")

    elif choice == "3":
        print("Спасибо за игру! До свидания.")
        break

    else:
        print("Некорректный ввод. Пожалуйста, выберите действие.")

    if not coins:
        print("Поздравляем! Вы собрали все монеты!")
        print("Вы победили!")
        break