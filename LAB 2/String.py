
#WAP to check the strings contains all the alphabets

#here we are checking the enter string that contains atleast 1 alphabet
def check(nt):
    alphabets="abcdefghijklmnopqrstuvwxyz"

    #for loop use for checking each letter in string
    for letter in alphabets:
        #if letter is present then continue otherwise return false
        if(letter in nt):
            continue
        else:
            return False
    return True
#Here user will enter the sentence
string=input("Please enter the string you want to check :")
#checking the string and return a copy of the string if all the alphabets are presents the return yes otherwise return no
if(check(string.lower())):
    print("Yes,this string contains all the alphabets")
else:

    print("No,this string not contains all the alphabets")