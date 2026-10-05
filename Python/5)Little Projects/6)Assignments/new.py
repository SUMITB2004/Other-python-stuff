# Smart Student Report Generator

def get_student_name(name):
    print("Enter student name: ")
    return name

def total_subject(n):
    try:
        if n <= 3 and n >=5:
            print("Enter Total subject(between 3 and 5): ")
            return n
        else:
            print("please enter num between 3 and 5")
            
    except ValueError:
        print("invalid number")
    

def get_marks(marks, subject):
    subject = {}
    for i in range (1, subject+1):
        try:
            subject = input("Enter subject name: ")
            marks = int(input("Enter marks: "))
            if marks (0 <= marks >=100):
                print(marks)
            else:
                print("Enter marks between 0 to 100")
                break
        except:
            print("Enter valid subject or marks")


def grade(subject):
    mark_list = []




            



            
        
