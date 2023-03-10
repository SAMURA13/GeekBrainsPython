# words = input().split()
# vowels_count = list(map(lambda word: sum(map(lambda letter: letter.lower() in 'уеыаоэяию', word)), words))
# if all(x == vowels_count[0] for x in vowels_count):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')



def print_operation_table(operation, num_rows=6, num_columns=6):



    table = [[None] * num_columns for _ in range(num_rows)]


    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            table[i-1][j-1] = operation(i, j)


    for row in table:
        print('\t'.join(map(str, row)))

print_operation_table(lambda x, y: x * y)