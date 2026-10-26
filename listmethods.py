list = [ 12, 4, 10, 8]

list.append(7)
print(list.append(7))#returns None
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

list2 = ['apple', 'banana', 'cherry']
list2.sort()
print(list2)

list.reverse()
print(list)

list3 = [1, 2, 3, 4, 5]
list3.insert(2,10) #inserts 10 at index 2
print(list3)
list3.remove(4) #removes first occurrence of 4
print(list3)
list3.pop(1)
print(list3) #index 1 is removed