import random
 
words = [
    'яблоко', 'груша', 'виноград', 'апельсин', 'персик', 'банан', 
    'книга', 'лампа', 'стол', 'зеркало', 'окно', 'тумба', 'волк', 
    'медведь', 'лев', 'заец', 'лиса', 'жираф'
]

word = words[random.randrange(17)]
len_word = len(word)
health = 10
test = False
#Заполняю массив знаком '*'
secret_word = '*' * len(word)
win_word = list(secret_word)
used_letters="" 

print(f'Добро пожаловать в игру "Виселица"! \nПопробуйте угадать слово: {win_word}')
while len_word != 0 and health != 0:
    test = False
    while True:
        letter = input("Введите букву ")
        if letter in used_letters or len(letter)>1:
            print("\nНе больше одного символа, попробуйте снова!")
        else:
            used_letters+=letter
            break
#Меняю знак '*' на букву    
    count=0
    for i in word:
        if letter in i:
            len_word -= 1
            test=True
            win_word[count]=letter
        count+=1
 
    if not test:
        health -= 1
        print("Неверно")
    else:
        print("Верно")
        print(win_word)
 
    print(f'У вас осталось {health} попыток')
 
if(len_word == 0):
    print(f'Вы угадали с {health} попытки, слово - "{word}"')
else:
    print(f'ВЫ ПРОИГРАЛИ! Это слово: "{word}" \nПОПРОБУЙТЕ СНОВА!')