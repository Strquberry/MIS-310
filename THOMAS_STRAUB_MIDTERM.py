#Tom Straub
#Midterm
#Problem 1

#Define the main function, but do not call it the main function since all of the programs are on one file.
def check_temperature():
    print("Temperature Monitoring System")
    print("Target maximum temperature: 102.5°C")

    # Get initial temperature reading
    temp = float(input("Enter the current temperature in Celsius: "))

    # Check if temperature exceeds 102.5°C
    if temp <= 102.5:
        print(f"Temperature {temp}°C is within safe range.")
        print("Please wait 15 minutes and check temperature again.")
        input("Press Enter when ready to take next reading...")
        #check_temperature()  # Recursive call for next check
        #Repeating of the program is stopped so the rest of the problems can be run.

    #Create the else for if the temperature is too high
    else:
        print(f"WARNING: Temperature {temp}°C exceeds 102.5°C!")
        print("Please turn down the thermostat.")
        print("Please wait 5 minutes for temperature to stabilize.")
        input("Press Enter after 5 minutes to take new reading...")
        #After the user hits the enter key, rerun the program
        #I have commented out the repeating of this program so the other two problems can run.
        #check_temperature()

# Run the program
check_temperature()


#Problem 2

#Define a way to calculate the points
def calculate_points(books):
    if books >= 8:
        return 60
    #Repeat elif statements for each tier of points
    elif books >= 6:
        return 30
    elif books >= 4:
        return 15
    elif books >= 2:
        return 5
    #end the if loop for the user not getting any points
    else:
        return 0

#Define the main function
def main():
    print("Serendipity Booksellers Book Club")

    # Get number of books purchased
    books = int(input("Enter the number of books purchased this month: "))

    # Ensure non-negative input
    if books < 0:
        print("Number of books cannot be negative!")
        return

    # Calculate and display points
    points = calculate_points(books)
    print(f"For {books} books purchased, you earned {points} points!")

# Run the program
main()


#Problem 3


#Define the function for the input
def usernumber (n):
    # Handle special case of 0
    if n == 0:
        return 1

    # Calculate factorial using a for loop
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

#Define the input function
def get_factorial_input():
    print("Factorial Calculator")

    # Get user input
    user_input = input("Enter a nonnegative integer: ")

    # Validate input (using positive condition instead of if not)
    if user_input.isdigit():
        # Convert to integer and calculate
        number = int(user_input)
        result = usernumber(number)
        #print results for the user
        print(f"The factorial of {number} ({number}!) is {result}")

        #Create an else statement for invalid inputs
    else:
        print("Error: Please enter a valid nonnegative integer!")
        return get_factorial_input()  # Recursive call for invalid input


# Run the program
get_factorial_input()