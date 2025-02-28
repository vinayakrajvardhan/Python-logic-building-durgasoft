list = [9,3,5,6,7,2,1,234]
list1 =[1,2,3,4,5,6,7,8]
l = len(list)
m = len(list) //2

z = sorted(list[:m])
print(z)

for i in range(8):
  print(list[i]-list1[i],end=" ")