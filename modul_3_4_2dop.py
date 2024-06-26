def get_multiplied_digits(number):
    if number < 10:
        if number == 0:
            return 1
        return number
    str_number = str(number)
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))



number = int(input('Введите число: '))
print(get_multiplied_digits(number))