num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")





number_check_value = float(input("Enter a number: "))

if number_check_value > 0:
    print("The number is positive.")
elif number_check_value < 0:
    print("The number is negative.")
else:
    print("The number is zero.")





num_a = float(input("Enter the first number: "))
num_b = float(input("Enter the second number: "))
num_c = float(input("Enter the third number: "))

if num_a >= num_b:
    if num_a >= num_c:
        print("The greatest number is:", num_a)
    else:
        print("The greatest number is:", num_c)
else:
    if num_b >= num_c:
        print("The greatest number is:", num_b)
    else:
        print("The greatest number is:", num_c)





voter_age = int(input("Enter your age: "))
voter_nationality = input("Enter your nationality: ")

if voter_age >= 18 and voter_nationality.lower() == "indian":
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")





student_marks_value = float(input("Enter the student's marks: "))

if student_marks_value >= 90:
    print("Grade: A")
    
    # Nested condition for Excellent
    if student_marks_value > 95:
        print("Excellent")

elif student_marks_value >= 75:
    print("Grade: B")

elif student_marks_value >= 50:
    print("Grade: C")

else:
    print("Grade: Fail")







login_username_input = input("Enter username: ")
login_password_input = input("Enter password: ")

correct_username = "admin"
correct_password = "1234"

if login_username_input == correct_username:
    # Username is correct → now check password
    if login_password_input == correct_password:
        print("Login successful!")
    else:
        print("Wrong password.")
else:
    print("Username not found.")




units_consumed_value = int(input("Enter the number of units consumed: "))

total_bill_amount = 0

if units_consumed_value <= 100:
    total_bill_amount = units_consumed_value * 5

else:
    # More than 100 units
    if units_consumed_value <= 200:
        first_100_cost = 100 * 5
        remaining_units = units_consumed_value - 100
        total_bill_amount = first_100_cost