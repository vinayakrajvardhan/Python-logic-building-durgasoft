def count_digit(num):
    c = 0
    while num != 0:
        d = num % 10
        c = c + 1
        num = num // 10
    return c


pin = '1234'

print(count_digit(int(pin)))
valid = False

if pin.isdigit() and not pin.isspace() and count_digit(int(pin)) == 4:
    valid = True
else:
    valid = False

if valid:
    print('Valid ATM pin')
else:
    print('Not valid ATM pin')
