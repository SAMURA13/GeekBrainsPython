words = input().split()
vowels_count = list(map(lambda word: sum(map(lambda letter: letter.lower() in 'уеыаоэяию', word)), words))
if all(x == vowels_count[0] for x in vowels_count):
    print('Парам пам-пам')
else:
    print('Пам парам')