


#crete a list of tuple and sort it by last element in increasing order


#we have created a list of tuple
list = [(1, 6), (1, 7), (4, 5), (2, 2), (1, 3)]

#we have used the key parameter in sorted funtion and using only the last element in the tuple for comparing the elements
print (sorted(list, key=lambda x: x[-1]))