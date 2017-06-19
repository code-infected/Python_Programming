# Check whether a number entered by a user is even or odd


name="UMKC"

print('welcome to',name)
print ("Check whether a number entered by a user is even or odd")

num1 = int(input("Please enter a number :"))

num2 = num1 % 2

if num2 == 0:

    print(num1,": Given number is Even")


else:

    print(num1,": Given number is Odd")


print ('Thanks you. END')