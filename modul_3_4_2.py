def get_multiplied_digits(number, rezult = 1, number_of_turn = 0 ):
    if number < 10:
        if number_of_turn == 0:
            return number
        elif number == 0:
            return rezult
        else:
            return rezult * number
    str_number = str(number)
    first = int(str_number[0])
    rezult = rezult * first
    number_of_turn += 1
    return get_multiplied_digits(int(str_number[1:]), rezult, number_of_turn)


number = int(input('Введите число: '))
print(get_multiplied_digits(number))
