import random
import math


class Rating:
    def __init__(self, name):
        self._old_data = None
        self._user_name = name
        self.score = self._get()

    def _get(self):
        """Reads the user score from the file and returns it. If the data file is not found, creates it."""
        try:
            with open('rating.txt', 'r') as f:
                for line in f:
                    name, score = line.split()
                    if name == self._user_name:
                        self._old_data = line
                        return int(score)
            # if the user's name is not found, create it
            with open('rating.txt', 'a') as f:
                f.write(f'{self._user_name} 0')
            self._old_data = f'{self._user_name} 0'
            return 0
        except FileNotFoundError:  # need create file
            with open('rating.txt', 'w') as f:
                f.write(f'{self._user_name} 0')
            self._old_data = f'{self._user_name} 0'
            return 0

    def add(self, score):
        """Adds scores to existing ones."""
        self.score += score

    def save(self):
        """Saves data to a file"""
        with open('rating.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(
            self._old_data, f'{self._user_name} {self.score}\n')
        with open('rating.txt', 'w') as f:
            f.write(new_data)


class User:
    def __init__(self):
        self.name = ''
        self._hello_user()
        self.rating = Rating(self.name)

    def _hello_user(self):
        self.name = input('Enter your name: ').strip().replace(' ', '')
        print(f'Hello, {self.name}')


class Game:
    def __init__(self):
        self.RPS = {}
        self.user_choice = ''
        self.game_choice = ''
        self.result = ''
        self.user = User()

    def referee(self):
        """Defines the result of the game and returns it as a text value:
        'win' - user won, 'lose' - user lost, 'draw' - draw."""
        if self.user_choice == self.game_choice:
            return 'draw'
        elif self.user_choice in self.RPS.get(self.game_choice):
            return 'win'
        else:
            return 'lose'

    def result_processing(self):
        """Prints game result and adds scores to the user."""
        if self.result == 'draw':
            self.user.rating.add(50)
            print(f'There is a draw ({self.game_choice})')
        elif self.result == 'lose':
            print(f'Sorry, but computer chose {self.game_choice}')
        elif self.result == 'win':
            self.user.rating.add(100)
            print(f'Well done. Computer chose {self.game_choice} and failed')

    def generator(self, user_input):
        output = {}
        items = list(user_input.split(','))
        if len(items) == 1:
            return {'rock': ['paper'], 'paper': ['scissors'], 'scissors': ['rock']}
        double_items = items + items
        half_items = math.ceil(len(items) / 2)
        for i in range(len(items)):
            output[items[i]] = double_items[i + 1:i + half_items:1]
        return output

    def run(self):
        self.RPS = self.generator(input())
        print('Okay, let\'s start')
        while True:
            self.user_choice = input().strip()
            if self.user_choice == '!exit':
                break
            if self.user_choice == '!rating':
                print(f'Your rating: {self.user.rating.score}')
                continue
            if self.user_choice not in ['rock', 'paper', 'scissors']:
                print('Invalid input')
                continue
            self.game_choice = random.choice(list(self.RPS.keys()))
            self.result = self.referee()
            self.result_processing()
        self.user.rating.save()
        print('Bye!')


if __name__ == '__main__':
    game = Game()
    game.run()
