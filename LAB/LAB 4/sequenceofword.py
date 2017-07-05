

#Prints the unique words in sorted form from a comma separated sequence of words

#user will enter the seuence of word with seperate comma
List = input("Please enter the separated words with comma:  ")

#split funtion will split or break the word and the data to a string array using a seperater
enter_word = [word for word in List.split(",")]

#print the words in sorted form
print(",".join(sorted(list(set(enter_word)))))