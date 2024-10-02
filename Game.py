# *******************************Python Programming Assignment: Number Exploration Tool****************************************

# Prompting the user to enter their name
list1:list=[]
user_name:str=(input("enter your name:"))

# Ask them for three of their favorite numbers
for i in range(1,4):
    favourite_num=(int(input(f"{user_name} Kindly,enter your {i} favourite Number:")))
    list1.append(favourite_num)

# Greet the user with a personalized message that includes their name.
print(f"Hello, {user_name} ! Let's explore your favorite numbers:")

# stored in a list.
print(list1)

# Check if any of the numbers are even or odd 
for numbers in list1:
    if numbers%2==0:
        print(f"The number {numbers} is EVEN.")
    else:
        print(f"The number {numbers} is ODD")

# Create and print the list of numbers and their squares
print("\nHere are your numbers and their squares:")
for number in list1:
    square = number ** 2
    print(f"The number {number} and its square:({number},{square})")

# Calculate the sum of the numbers
total=sum(list1)

# Provide an encouraging message
print(f"Amazing!\nThe sum of your three favorite numbers is: {total}")

# Check if the sum is a prime number.
#***********************Method NO 1*************************************
if total <= 1:
    print(f"{total} is not a prime number, but it's still a cool number!")
else:
    for i in range(2,total):
        if total% i == 0:
            print(f"{total} is not a prime number, but it's still a cool number!")
            break
    else:
        print(f"Wow, {total} is a prime number! That's awesome!")
#***********************Method NO 2*************************************#
is_prime=True
if total <= 1:
    is_prime=False
else:
    for i in range(2,total):
        if total%i==0:
            is_prime=False

if is_prime==True:
    print(f"Wow, {total} is a prime number! That's awesome!")
else:
    print(f"{total} is not a prime number, but it's still a cool number!")
    







