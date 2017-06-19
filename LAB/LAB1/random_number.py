#importing library to use random number generator module
import random

print(" Ask the number")
score = 10


#pick any random number
random_number = int(random.randint(0,9))


#for counting the number of game he can play
count = 1


print("Guess 1st chance")

num = input("Just guess the number")


n = int(num)


while(n!=random_number):
    if (n<random_number):
        print("Sorry!Please try again... this number is les sthen the guessed one")


    else:
        print("Sorry!Please try again... this number is les sthen the guessed one")


    count = count + 1

    print("Turn", count, ":")

    num = input("Guess the number picked by the system:")


    n = int(num)


if (count == 1):
    print("Congratulations! You guessed the correct one", score)
else:
    print("You have guessed the number correctly in", count, " your score is ",(score-count+1), ".")

    print("The number picked is:", random_number)