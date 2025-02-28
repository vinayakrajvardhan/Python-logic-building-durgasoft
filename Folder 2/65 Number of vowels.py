str = 'The quick brown fox jumps over the lazy dog'

vowels = ['a', 'i', 'e', 'o', 'u']
v = 0
c = 0
for i in str:
    if i in vowels:
        v = v + 1
    else:
        c = c + 1

print(f'consonant:{c}')
print(f'vowels:{v}')
