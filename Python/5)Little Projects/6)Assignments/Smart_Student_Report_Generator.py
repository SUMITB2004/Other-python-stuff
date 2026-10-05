# Smart Student Report Generator

def get_student_name():
    name = input("Enter student name: ").strip()
    return name


def get_number_of_subjects():
    while True:
        try:
            num = int(input("Enter number of subjects (3-5): "))
            if 3 <= num <= 5:
                return num
            else:
                print("Please enter a number between 3 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_marks(num_subjects):
    subjects = {}
    
    for i in range(1, num_subjects + 1):
        while True:
            try:
                subject_name = input(f"Enter name of subject {i}: ").strip()
                marks = float(input(f"Enter marks for {subject_name}: "))
                
                if 0 <= marks <= 100:
                    subjects[subject_name] = marks
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter numeric marks.")
    
    return subjects


def calculate_results(subjects):
    marks_list = list(subjects.values())
    total = sum(marks_list)
    average = total / len(marks_list)
    
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    return total, average, grade


def save_report_to_file(name, subjects, total, average, grade):
    filename = f"{name}_report.txt"
    
    try:
        with open(filename, "w") as file:
            file.write("===== Student Report =====\n")
            file.write(f"Name: {name}\n\n")
            
            file.write("Subjects and Marks:\n")
            for subject, marks in subjects.items():
                file.write(f"{subject}: {marks}\n")
            
            file.write("\n")
            file.write(f"Total: {total}\n")
            file.write(f"Average: {average:.2f}\n")
            file.write(f"Grade: {grade}\n")
        
        print(f"\nReport successfully saved as '{filename}'")
    
    except Exception as e:
        print("Error saving file:", e)


def main():
    print("===== Smart Student Report Generator =====")
    
    name = get_student_name()
    num_subjects = get_number_of_subjects()
    subjects = get_marks(num_subjects)
    
    total, average, grade = calculate_results(subjects)
    
    print("\n===== Result =====")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
    
    save_report_to_file(name, subjects, total, average, grade)


# Run the program
if __name__ == "__main__":
    main()
