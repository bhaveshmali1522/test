s = "bhvaesh"

# using for loop with string
for i in s:
    print(i)




for i in range(0, 10, 2):
    print(i)

#
l1 = ["eat", "sleep", "repeat"]
#
for count, ele in enumerate(l1):
    print (count, ele)

#
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


#
Numbers =[x for x in range(11)]
print(Numbers)

#
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)