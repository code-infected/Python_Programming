
#program that print the first letter of your name with star


#for initilizing row and we have taken range from 0 to 6
for i in range (7):

#for intitilizing coloumn,we have taken range from 0 to 4
    for j in range (5):

        #we need star when column = 0 and column = 4 to print Letter A but that time row should not equal to 0
        #when row = 0 and row = 3 then column >0 and less then 4
        if (j == 0 or j == 4) or ((i == 0 or i ==3)and (j>0 and j<4)):
            #print * and then i mention empty string i dont want any new line
            print("*",end="")
        else:
            #print space
         print(end=" ")
    #control will goes to new line to execute new line
    print()