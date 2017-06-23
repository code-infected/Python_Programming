#Accept a String from a user and then convert each character in the string to a item in list and tuple.



#user can enter any string
String = input("Please enter any string :")

#tuple we are using to print the number in string
Mytuple = tuple(String)

#creating a list for converting each charachter and print in list
list=[]

#intilizing for loop 
for char in String:

    #using append function to split a string
    list.append(char)
#print the list and tuple
print (list)
print(Mytuple)

