# Program for reversing a number

num = int(input("Please Enter a number : ")) #Enter the number you want to get reverse

Reverse = 0 #intilization

while num > 0:

 Reminder = num %10
 Reverse = (Reverse *10) + Reminder
 num = num //10

print("Reverse of a given enter number is = %d" %Reverse)