#*********BASIC CALCULATOR************

# Method 01
print(eval(input("enter your expression:")))

# Method 02
value1=float(input("Enter your first value:"))
value2=float(input("Enter your second value:"))
opr=input("operations:+,-,*,/")

if   opr== "+": # type: ignore
    print(value1,"+",value2,"=",value1+value2)
elif opr=="-": # type:ignore
    print(value1,"-",value2,"=",value1-value2)
elif opr=="*": # type:ignore
    print(value1,"*",value2,"=",value1*value2)
elif opr=="/": # type:ignore
    print(value1,"/",value2,"=",value1/value2)
else:
    print("Invalid operation")
    
# Method 03
value01=input("Enter your expression")
result=(eval(f"{value01}"))
print(f"{result}")

# Method 04
a=float(input("first value:"))
b=float(input("second value:"))
opr=input("operations: +,-,*,/")

if opr== "+" :
    print (a ,"+",b , "=" ,a+b)
if opr== "-":
    print (a ,"-",b , "=" , a-b)
if opr== "*":
    print (a ,"*",b , "=" , a*b)
if opr== "/":
    print (a ,"/",b , "=" , a/b)
if opr !="+"and opr !="-"and opr !="*"and opr !="/":
    print("invalid operation")



 


