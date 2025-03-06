hex_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def hex_to_decimal(hex_num):
    exp = len(hex_num) - 1
    decimal_num = 0
    for i in range(len(hex_num)):
        decimal_num += (16**exp * hex_dict[hex_num[i]])
        exp -= 1
    return decimal_num

def decimal_to_binary(dec_num):
    binary = ''
    while dec_num > 0:
        remain = dec_num % 2
        dec_num = dec_num // 2
        binary = str(remain) + binary
    return binary

print(hex_to_decimal('FF'))
print(decimal_to_binary(31))