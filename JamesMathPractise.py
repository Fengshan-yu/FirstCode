# This is the very first program I wrote up since studying Python on November 10, 2021.
# This is for my son, a first grader, to practice Math.

test = input("DO you want practise Plus or Minus?: ")

if test == str("+"):
    A = int(input("Enter a number: "))
    B = int(input("Enter another number: "))
    result = input(str(A) + " + " + str(B) + " = ? : ")
    if result == str(A + B):
        print("Congratulations, you are right.")
    else:
        print("Incorrect, try again.")

elif test == str("-"):
    A = int(input("Enter a number: "))
    B = int(input("Enter another number: "))
    result = input(str(A) + " - " + str(B) + " = ? : ")
    if result == str(A - B):
        print("Good, you are right.")
    else:
        print("Not right, try again.")

else:
    print("Invalid Input.")

