# 🎯 **_Python programming_** 🎯

## **Assignment: Number Exploration tool**

---

### Welcome to python exploration tool😎

In this assignment, we will explore the interesting chracteristics of your favorite numbers! You will enter three of your favorite numbers, and this tool will analyze them by checking if they are even or odd, calculate their squares, calculate their sum, and check if the sum is a prime number or NOT! 🤓

## _🚀 Features of the Tool:_

- ✅ _Personalized User Greeting_
- ✅ _Input and Store Favorite Numbers_
- ✅ _Even/Odd Number Detection_
- ✅ _Calculation of Squares of Numbers_
- ✅ _Sum of Numbers_
- ✅ _Checking it's prime number or not_

---

### _1️⃣ 📑 Code Structure:_

The following sections describe the structure of the code used in the Number Exploration Tool.👇👇

### _2️⃣ Collecting User Information:_

- We first prompt the user to input their name

```python
list1:list=[]
user_name:str=(input("enter your name:"))
```

### _3️⃣ Favorite Numbers Input:_

The user is asked to input three of their favorite numbers, which are stored in a list

```python
for i in range(1,4):
    favourite_num=(int(input(f"{user_name} Kindly,enter your {i} favourite Number:")))
    list1.append(favourite_num)
```

### _4️⃣ Greet them with a personalized message:_

```Python
print(f"Hello, {user_name} ! Let's explore your favorite numbers:")

# stored in a list.
print(list1)
```

### _5️⃣ Checking Even or Odd:_

The tool checks each number to find out that if it is even or odd as output.

```python
for numbers in list1:
    if numbers % 2 == 0:
        print(f"The number {numbers} is EVEN.")
    else:
        print(f"The number {numbers} is ODD.")
```

### _6️⃣ Calculating and Displaying Squares:_

The squares of each of the user's favorite numbers are calculated and displayed as output.

```python
for number in list1:
    square = number ** 2
    print(f"The number {number} and its square: ({number}, {square})")
```

### _7️⃣ Calculating the sum of Numbers:_

The sum of all three numbers is calculated and printed,accompanied by an encouraging message.

```python
total = sum(list1)
print(f"Amazing!\nThe sum of your three favorite numbers is: {total}")
```

### _8️⃣ Checking for Prime Numbers:_

#### Method 1:

A simple **IF-ELSE** method is implemented using loops.

```python
if total <= 1:
    print(f"{total} is not a prime number, but it's still a cool number!")
else:
    for i in range(2, total):
        if total % i == 0:
            print(f"{total} is not a prime number, but it's still a cool number!")
            break
    else:
        print(f"Wow, {total} is a prime number! That's awesome!")
```

#### Method 2:

A more advanced method is used to check for primes with a boolean flag.

```python
is_prime = True
if total <= 1:
    is_prime = False
else:
    for i in range(2, total):
        if total % i == 0:
            is_prime = False

if is_prime:
    print(f"Wow, {total} is a prime number! That's awesome!")
else:
    print(f"{total} is not a prime number, but it's still a cool number!")
```

---

### 🔍 Output Example:

Here is an example of what the output will look like when the program is run:

```vb
Enter your name:Haseeb Ahmed
Haseeb Ahmed Kindly,enter your 1 favourite Number:2
Haseeb Ahmed Kindly,enter your 2 favourite Number:3
Haseeb Ahmed Kindly,enter your 3 favourite Number:8
Hello, Haseeb Ahmed ! Let's explore your favorite numbers:
[2, 3, 8]
The number 2 is EVEN.
The number 3 is ODD
The number 8 is EVEN.

Here are your numbers and their squares:
The number 2 and its square:(2,4)
The number 3 and its square:(3,9)
The number 8 and its square:(8,64)
Amazing!
The sum of your three favorite numbers is: 13
Wow, 13 is a prime number! That's awesome!
Wow, 13 is a prime number! That's awesome!
```

---

## **📌 Key Components:**

| Component                   | Description                                                      |
| --------------------------- | ---------------------------------------------------------------- |
| **User Input**              | The user enters their name and favorite numbers.                 |
| **Even/Odd Check**          | Determines whether each number is even or odd.                   |
| **Square Calculation**      | Computes and displays the square of each favorite number.        |
| **Sum Calculation**         | Calculates the total sum of the favorite numbers.                |
| **Prime Check (2 methods)** | Verifies if the sum of the numbers is a prime using two methods. |

---

## **🎯Key Checkpoints:**

- Name input and personalized greeting
- List stores favorite numbers
- Checks even/odd for each number
- Squares of the numbers calculated and displayed
- Sum of the numbers computed
- Checks if the sum is prime using two different methods

---

**Thank you for using the _Number Exploration Tool_!** 🎉  
Feel free to try it with different numbers and explore their unique properties!

> **Happy coding! 😊**

---

### **Credits:**

**Developed by:** Haseeb Ahmed
