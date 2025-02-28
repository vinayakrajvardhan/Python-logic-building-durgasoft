num = '123564'

n = list(num)
valid_ticket = False
for i in range(len(num) - 1):
   if abs(int(num[i + 1]) - int(num[i])) <= 2:
       valid_ticket = True
   else:
       valid_ticket = False

if valid_ticket:
    print('valid ticket')
else:
    print('Invalid ticket')