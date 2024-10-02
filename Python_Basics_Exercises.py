# 1.Simple Message
# Assign a message to a variable and print that message
a:str="haseeb ahmed"
print(a)
# 2-Simple Messages
# Assign a message to a variable and print that message
h:str="hello world"
print(h)
# Change the value of the variable to a new message, and print the new message
b:str="hy how are you?"
print(b)
# 3. Personal Message
# Use a variable to represent a person’s name.
Name:str="Eric holland"
# Print a message to that person such as, “Hello Eric, would you like to learn some Python today?"
print(f"Hello {Name},would you like to have some tea")
# 4.Name Cases
# Use a variable to represent a person’s name.
name:str="Haseeb ahmed"
# Print the person’s name in lowercase, uppercase, and title case.
print(name.lower())
print(name.upper())
print(name.title())
# 5.Famous Quote
# Find a quote from a famous person you admire.
person:str="Nicola tesla"
Quote:str="The present is theirs; the future, for which I really worked, is mine."
# Print the quote and the name of its author.
print(f'{person} once said,"{Quote}"')
# 6. Famous Quote 2
# Use a variable called famous_person to represent the famous person’s name.
famous_person:str="Stephen hawking"
# Compose the message and represent it with a variable called message
message:str="""Remember to look up at the stars and not down at your feet. Try to make sense of what you see and wonder about what makes the universe exist. 
Be curious. And however difficult life may seem, there is always something you can do and succeed at. It matters that you don’t just give up."""
# Print the message
print(f'"{famous_person} said,{message}"')
# 7. Stripping Names
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
person1:str= "    haseeb    "
# Make sure you use each character combination, \t and \n, at least once.
person2:str="  haseeb \n\tAhmed  " 
# Print the name once, so the whitespace around the name is displayed.
print(person1)
print(person2)
# Print the name using each of the three stripping functions: lstrip(), rstrip(), and strip().
print(person1.lstrip())
print(person1.rstrip())
print(person1.strip())
print(person2.lstrip())
print(person2.rstrip())
print(person2.strip())
# 8.Variable Sum
# Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum
x:int=5
y:int=10
z:int=15
sum=x+y+z
print(sum)
# 9. Variable Swap
# Swap the values of two variables a and b. Print the values before and after the swap.

# Before swapping

c:int=1
d:int=4
print(f"before swap c={c}and d={d}")

# After swapping
d,c=c,d
print(f"After swap c={c}and d={d}")
# OR

# Before swapping
temp:int
c=1
d=4
print(f"before swap c={c}and d={d}")
# After swapping
temp=c
c=d
d=temp
print(f"After swap c={c}and d={d}")


# 10. Favorite Color
# Create a variable with your favorite color and print it. Then change the variable name to something else and print the color again.
color:str="black"
print("favorite color:",color)
color_name=color 
print(color_name)
# 11.Changing Pet Name
#  Create a variable pet_name and set it to "Buddy". Change the value of pet_name to "Max" and print the new value
pet_name:str="Buddy"
pet_name="Max"
print(pet_name)
# 12.Observing Name Error
# Assign the value "Sunshine" to a variable and print it. Then, mistakenly try to print a variable with a different name (like sunsine) and observe the error
sky:str="sunshine"
print(sky)
# NameError: name 'Sky' is not defined.

# 13.Reassigning Score
# Assign the value 100 to a variable score and print it. Then assign a new value to score and print it again.
score:int=100
print(score)
score=50
print(score)
# 14.City Name
# Create a string variable city and assign it the name of a city you like. Print the city name.
city:str="Lahore"
print(city)
# 15.Title Case Text
# Task: Create a variable text with the value "python programming" and print it in title case.
text:str="python programming"
print(text.title())
# 16.Lowercase Conversion
# Task: Assign a string with mixed cases to a variable and print it in all lowercase letters
Text:str="My name Is HASEEb ahmeD"
print(Text.lower())
# 17.Uppercase Conversion
# Task: Assign a string with mixed cases to a variable and print it in all uppercase letters.
text="My name Is HhASEEb ahmeD"
print(text.upper())
# 18.Current Temperature
#Task: Create a variable temperature with the value 25. Print "The current temperature is [temperature] degrees." using the variable.
Temperature:int=25
print("The current temperature is",Temperature,"degrees")
#19. Printing a Poem
#Task: Create a variable poem with a short poem that has multiple lines. Print the poem with each line starting on a new line.
poem:str="""Beneath the sky, where dreams take flight,
In whispered winds of endless night,
Stars weave tales of hope and light,
Guiding hearts to morning bright."""
print(poem)

Poem:str="Beneath the sky, where dreams take flight,\nIn whispered winds of endless night,\nStars weave tales of hope and light,"
print(Poem)

























