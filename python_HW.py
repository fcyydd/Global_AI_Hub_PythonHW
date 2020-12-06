from random import randint

def check_name(argument):
    """
    Checks input char by char if it contains number, .. etc.!
    """
    for char in argument:
        if char.isalpha() == False:
            if char.isspace() == False:
                return False
    return True

def lessons_push():
    """
    Takes lessons as input!
    """
    lessons = list()
    print("Enter lessons (-1 to exit): ")
    x = input()
    while x != '-1':
        lessons.insert(0, x)
        x = input()
    return lessons

def check_lessons(lessons):
    """
    Returns whetherif the student passed or failed the class!
    """
    if len(lessons) < 3:
        return "You failed in class"
    else:
        return True

def assign_grades():
    """
    Assigning grades randomly!
    """
    lesson = {
        "midterm": randint(1,100),
        "final": randint(1,100),
        "project": randint(1,100)
    }
    return lesson

def final_grade(grades):
    """
    Calculates the final grade which we need later to check the student passed or failed, and returns!
    """
    return (grades["midterm"]*30/100) + (grades["final"]*50/100) + (grades["project"]*20/100)

def passed_or_failed(grade):
    """
    Determines a course passing grade acoording to the argument!
    """
    if int(grade) >= 90:
        print("AA")
    elif int(grade) < 90 and int(grade) >= 70:
        print("BB")
    elif int(grade) < 70 and int(grade) >= 50:
        print("CC")
    elif int(grade) < 50 and int(grade) >= 30:
        print("DD")
    else:
        print("FF")
    pass


#MAIN!


name = input("Name && surname: ")
check = check_name(name)
for x in range(1,4):
    check = check_name(name)
    if check == False:
        print("Try again!")
        name = input("Name && surname: ")

if check == False:
    print("Please try again later")
else:
    print("Welcome")
    list_of_lessons = lessons_push()
    if check_lessons(list_of_lessons) == True:
        print("Choose a lesson to take its exam!")
        chosen = input()
        #Students cannot assign their grades so I'll assign grades randomly!
        if chosen not in list_of_lessons:
            print("Wrong lesson name! Type again!")
            #Student must enter the lesson's name correctly!
            while True:
                chosen = input()
                if chosen in list_of_lessons:
                    break
        chosen = assign_grades()
        final = final_grade(chosen)
        passed_or_failed(final)
    else:
        print(check_lessons(list_of_lessons))
     