import random


class GuessingGame:
    def __init__(self, min_number, max_number, attempts, initial_capital):
        self.min_number = min_number
        self.max_number = max_number
        self.attempts = attempts
        self.initial_capital = initial_capital
        self.current_capital = initial_capital
        self.target_number = random.randint(min_number, max_number)

    def start(self):
        print(f"Добро пожаловать в игру 'Угадай число'!")
        print(f"У вас есть {self.attempts} попыток, чтобы угадать число от {self.min_number} до {self.max_number}.")
        print(f"Начальный капитал: {self.initial_capital}")

        for attempt in range(1, self.attempts + 1):
            if self.current_capital <= 0:
                print("Ваш капитал закончился. Игра окончена.")
                break

            print(f"\nПопытка {attempt}. Ваш текущий капитал: {self.current_capital}")
            bet = self.get_bet()

            guess = int(input("Введите ваше предположение: "))

            if guess == self.target_number:
                self.current_capital += bet
                print(f"Поздравляем! Вы угадали число. Ваш выигрыш: {bet}. Новый капитал: {self.current_capital}")
                break
            else:
                self.current_capital -= bet
                print(f"Неверно. Вы потеряли ставку: {bet}. Оставшийся капитал: {self.current_capital}")

            if attempt == self.attempts:
                print("Вы исчерпали все попытки. Игра окончена.")
                print(f"Загаданное число было: {self.target_number}")

    def get_bet(self):
        while True:
            try:
                bet = int(input("Введите вашу ставку: "))
                if bet > 0 and bet <= self.current_capital:
                    return bet
                else:
                    print("Ставка должна быть положительной и не превышать текущий капитал.")
            except ValueError:
                print("Пожалуйста, введите корректное число.")
