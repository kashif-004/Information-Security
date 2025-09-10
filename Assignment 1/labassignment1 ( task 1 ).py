list1 = []
for i in range(2):
    value = int(input("Enter a Number: "))
    list1.append(value)



list2=[]

for i in range(2):
    value = int(input("Enter an another number: "))
    list2.append(value)

list1.extend(list2)
list1.sort()
print(list1)


