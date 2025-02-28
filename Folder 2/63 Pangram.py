str = 'The quick brown fox jumps over the lazy dog'

alp = "abcdefghijklmnopqrstuvwxyz"
pangram = False
for i in str.lower():
    if i in alp:
        pangram = True
    else:
        pangram = False

if pangram:
    print('Pangram')
else:
    print('Not pangram')