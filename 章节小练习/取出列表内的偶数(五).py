#取出list中的偶数放入另一个列表中
#for循环
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = list()
for i in list_1:
    if i % 2 == 0:
        list_2.append(i)
print(list_2)

#while循环
list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_4 = []
index = 0
while index < len(list_3):
    if list_3[index] % 2 == 0:
        list_4.append(list_3[index])
    index = index + 1
print(list_4)