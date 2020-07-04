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
    letter = input('введите одну русскую букву ').lower()
    # TODO letter validation
    if len(letter) != 1:
        continue
    if letter in secret_word:
        pass
    else:
        #pass
        print(f'ошибок допущено', errors_counter)
        errors_counter += 1
    print('вы ввели ', letter)
    if errors_counter > 3:
        print(f"haha you are louser with {errors_counter} errors")
        break
