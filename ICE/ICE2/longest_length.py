
#Enter a list of words and returns the length of the longest one

def main():
    String = input("Please Enter a list of words : ")

    longest = 0

    for words in String.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words

    print(longest_word, "is the longest word with length", len(longest_word))

main()