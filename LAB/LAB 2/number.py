

#Python program to find those numbers which are divisible by 7 and multiple of 5


#First of all user should be able to enter the lower as well as upper limit
lower_value=int(input("Please enter the lower value range:"))
upper_value=int(input("Please enter the upper value range:"))

#for loop will use to range the lower value number to the upper value number
for k in range (lower_value,upper_value+1):

    #if the remainder of k is divisible by 5/7 is equal to 0 then k should be print
    if(k%7==0 and k%5==0):
        print(k)