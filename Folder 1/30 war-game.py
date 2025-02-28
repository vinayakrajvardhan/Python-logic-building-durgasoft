war_list:list[int] = list(input("Enter the value"))
print(war_list)

sum_odd = sum_even = 0

for i in war_list:
    if int(i) % 2 == 0:
        sum_even = sum_even + int(i)
    else:
        sum_odd = sum_odd + int(i)

print(sum_odd)
print(sum_even)
print(abs(sum_even-sum_odd))