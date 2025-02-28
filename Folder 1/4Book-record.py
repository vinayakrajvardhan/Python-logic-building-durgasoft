book_share:int = int(input("Enter the range:"))

if book_share in range(30,50):
    print('D')
elif book_share in range(51,60):
    print('C')
elif book_share in range(61,80):
    print('B')
elif book_share in range(81,1000):
    print('A')