def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Student Name:")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = input("Enter Math Score:")
    science_score = input("Enter Science Score:")
    english_score = input("Enter English Score:")

    # Calculate the average grade
    average_grade = ((int(math_score) + int(science_score) + int(english_score)) / 3)
    # Adding formatting to print to 2 decimal places
    output = f"{average_grade:.2f}"
    #Print statements with new formatting
    print("Student Name:" , student_name)
    print("Average Grade:" , average_grade)


    # Return the student's name and their average grade
    return (student_name, average_grade)

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"You can do better," , student_name, average_grade, "is alright.")