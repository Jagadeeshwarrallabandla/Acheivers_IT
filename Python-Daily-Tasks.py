#Task on 6/05/2024

'''def registration_for_course(name,qualification,passedout,courselooking,amount):
    user_name = name
    user_qualification = qualification
    user_passedout_year = passedout
    user_looking_for = courselooking
    amount_of_course = amount
    print(f"{user_name} has completed his {user_qualification} in {user_passedout_year}, So he enrolled for {user_looking_for} by paying {amount_of_course} as his first installment Fee")
all_registration_details = ("Jagadeeshwar","B-Tech",2024,"Full Stack Python",15000)
registration_for_course(*all_registration_details)'''

'''input_value = input("Enter the Character  : ")
lowe_case = input_value.lower()
print(f"Your Character is {lowe_case}")
def palindrome_or_not():
    removing_non_alphabets = ''.join(c for c in input_value if c.isalnum())
    print(removing_non_alphabets)
    reversing = removing_non_alphabets[::-1]
    print(f"after palindrome {reversing}")
    if (input_value == reversing ):
        print("Yes it is a palindrome ", reversing)
    else :
        print("Not a Palindrome" ,reversing )
palindrome_or_not()'''

'''def primenumber_not(number):
    if number <= 1:
        print(f"0 and 1 are neither prime numbers")
        return False
    for i in range(2, 100):
        if number % i == 0:
            print(f"The given number {number} is not a prime number")
            return False
    print(f"The given number {number} is a prime number")
    return True

number_value = int(input("Enter the Number = "))
primenumber_not(number_value)'''

def factorial(n):
    """
    Find the factorial of a given number using recursion.

    Args:
    n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n times factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
number = 5
print("Factorial of", number, "is:", factorial(number))



    