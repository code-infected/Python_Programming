
#Write a program to replace the dictonary value with their sum

def course_GPA (list):

    for i in list:
        n1 = i.pop('LastGPA')
        n2 = i.pop('CurrentGPA')
        i['LastGPA+CurrentGPA'] = (n1 + n2)/2 #here we are adding last+current GPA
    return list

course_current_finalGPA= [
  {'course' : 'python',  'LastGPA' : 90, 'CurrentGPA' : 80},
{'course' : 'python',  'LastGPA' : 95, 'CurrentGPA' : 85},
{'course' : 'python',  'LastGPA' : 100, 'CurrentGPA' : 100},

]
print(course_GPA(course_current_finalGPA))