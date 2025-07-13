#Task 1: Perform Basic Mathematical Operations
#Problem Statement: Write a Python program that does the following:
#1.  Takes two numbers as input from the user.
#2.  Performs the basic mathematical operations on these two numbers:
#o	Addition
#o	Subtraction
#o	Multiplication
#o	Division
#3.  Displays the results of each operation on the screen.
# Expected Output:
#The output should include the result of each operation performed, for example:

x=int(input("Enter First interget :"))
y=int(input("Enter Second interget :"))
a=x+y
s=x-y
m=x*y
d=x/y
print("Addition:",a)
print("Subtraction:",s)
print("Multipication:",m)
print("Divide:",d)

#Task 2: Create a Personalized Greeting
#Problem Statement: Write a Python program that:
#1.  Takes a user's first name and last name as input.
#2.  Concatenates the first name and last name into a full name.
#3.  Prints a personalized greeting message using the full name.
#Expected Output:
#The program should output a greeting like:
f_name=input("Enter Your First name >>>")
l_name=input("Enter Your Second name >>>")
A_name=f_name+" "+l_name
print(A_name)
