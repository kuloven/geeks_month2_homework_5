from decouple import Config, Csv, config
from logic import GuessingGame


def main():
    min_number = config('MIN_NUMBER', cast=int)
    max_number = config('MAX_NUMBER', cast=int)
    attempts = config('ATTEMPTS', cast=int)
    initial_capital = config('INITIAL_CAPITAL', cast=int)

    game = GuessingGame(min_number, max_number, attempts, initial_capital)
    game.start()


if __name__ == '__main__':
    main()
