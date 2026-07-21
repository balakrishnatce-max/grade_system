def calculate_grade(mark):
    if mark >= 90 and mark <= 100:
        return "A"
    elif mark >= 80 and mark <= 89:
        return "B"
    elif mark >= 70 and mark <= 79:
        return "C"
    elif mark >= 60 and mark <= 69:
        return "D"
    elif mark > 100 or mark < 0:#to handle invalid marks(-ve or greater than 100)
        return "Invalid mark. Please enter a mark between 0 and 100."
    else:
        return "E"

try:
    mark = int(input("Enter your mark: "))
    grade = calculate_grade(mark)
    print("Your grade is:", grade)
except ValueError:#to handle invalid input like string data
    print("Invalid input. Please enter a valid number.")
