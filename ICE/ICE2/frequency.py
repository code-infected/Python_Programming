
#Calculate character frequency in a string

def frequency_char(string):
    dict = {}
    for i in string:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(frequency_char('Python Programming'))