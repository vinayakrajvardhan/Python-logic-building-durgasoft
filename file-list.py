list = [1,2,3,4,5]

st = '1234'
print(st.isdigit())

with open('list-text','w') as file:

    for i in list:
       file.write(str(i) + '\n')