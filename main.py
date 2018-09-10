# easy 1
var_1 = 1
var_2 = 'string'
var_3 = ('cort', 'cort_1')
var_4 = {'key': 'rez'}
var_5 = ['one']

var_input = input('Please, enter any text: ')
print('You input this text: ', var_input)

# easy 2

input_num = int(input('Please, enter any number: '))
print(input_num)

# easy 3

age = int(input('Please, enter you age: '))
if age < 18:
    print('Извините, пользование данным ресурсом только с 18 лет')
else:
    print('Доступ разрешен')

# normal 1

random_num = int(input('Enter any number: '))
while 0 > random_num > 10:
    random_num = int(input('Number not correct, 0 < number < 10, try again: '))
print(random_num ** 2)

# normal 2

input_var1 = int(input('Please, enter first number: '))
input_var2 = int(input('Please, enter second number: '))

input_var1 += input_var2
input_var2 = input_var1 - input_var2
input_var1 -= input_var2

print(input_var1, ' ', input_var2)

# hard 1

text_rez = ['хорошее состояние', 'следует заняться собой', 'стоит обратиться к врачу!']
surname = input('Введите фамилию: ')
name = input('Введите имя: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес в кг: '))
if age < 30:
    if 50 < weight < 120:
        rez = 0
    else:
        rez = 1
elif 30 > age > 50:
    if 50 < weight < 120:
        rez = 0
    else:
        rez = 1
else:
    if 50 < weight < 120:
        rez = 0
    else:
        rez = 2

print(name, surname, ', возраст:', age, ', вес:', weight, 'кг -', text_rez[rez])
