def addNum():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    z=x+y
    print(z)

def subNum():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    z=x-y
    print(z)

def mulNum():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    z=x*y
    print(z)

def divNum():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    z=x/y
    print(z)
do=True
while do:
    print("This is a basic calci")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("Please pick up an option")
    textInput=int(input())

    if(textInput==1):
        addNum()
    elif(textInput==2):
        subNum()
    elif(textInput==3):
        mulNum()
    elif(textInput==4):
        divNum()
    else:
        print("Please pick a valid number")
    print("continue?")
    ch=input()
    if ch!='y' and ch!='Y':
        do=False


