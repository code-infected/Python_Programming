
#Enter string and calculate the number of digits and letters

string = input("Please enter any Alphanumeric value :")

Digit=Letter=0

for i in string:

    if i.isdigit():
        Digit=Digit+1
    elif i.isalpha():
        Letter=Letter+1

print("Number of Letters is:", Letter)
print("Number of Digits is:", Digit)