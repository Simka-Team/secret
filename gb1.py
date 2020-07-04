import random

words_bank = ['автострада', 'бензин']

secret_word = random.choice(words_bank)

print(secret_word)

game_word = ['*'] * len(secret_word)

print(game_word)

game_word[2] = 'a'

print(game_word)

print(''.join(game_word))

errors_counter = 0 

while True:
    letter = input('введите обну русскую букву ').lower()
    # TODO letter validation
    if len(letter) != 1:
        continue
    if letter in secret_word:
        pass
    else:
        #pass
        print(f'ошибок допущено', errors_counter)
    print('вы ввели ', letter)