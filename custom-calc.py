# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!



import math

print("Welcome to the pythagorean theorem calculator (a^2 + b^2 = c^2)")
typeVar = input("Enter which variable you would like to solve for. You can either enter \"a\", \"b\", or \"c\": ")

#check if typeVar is either a, b, or c
while typeVar != "a" and typeVar != "b" and typeVar != "c":
    print("")
    print("Please enter either \"a\", \"b\", or \"c\"")
    typeVar = input("Enter which variable you would like to solve for. You can either enter \"a\", \"b\", or \"c\": ")

a = None
b = None
c = None

def isNum(num):
    try:
        int(num)
        return True 
    except:
        return False
   
def getA():
    #value for b
    b = input("Please enter a value for b: ")
    while isNum(b) != True:
        print("")
        print("Please enter a numeric value")
        b = input("Please enter a value for b: ")

    #value for c   
    print("")
    c = input("Please enter a value for c: ")
    while isNum(c) != True:
        print("")
        print("Please enter a numeric value")
        c = input("Please enter a value for c: ")

    #convert b and c to ints
    b = int(b)
    c = int(c)

    a = math.sqrt((math.pow(c, 2) - math.pow(b, 2)))
    
    # print((math.pow(2, 2)))
    print(f"A triangle, given leg \"b\" as {b} and a hypotenuse of {c} will result in leg \"a\" being {a}")

def getB():
    #value for a
    a = input("Please enter a value for a: ")
    while isNum(a) != True:
        print("")
        print("Please enter a numeric value")
        a = input("Please enter a value for a: ")

    #value for c
    print("")
    c = input("Please enter a value for c: ")
    while isNum(c) != True:
        print("")
        print("Please enter a numeric value")
        c = input("Please enter a value for c: ")

    #convert a and c to ints
    a = int(a)
    c = int(c)

    b = math.sqrt((math.pow(c, 2) - math.pow(a, 2)))
    print(f"A triangle, given leg \"a\" as {a} and a hypotenuse of {c} will result in leg \"b\" being {b}")

def getC():
    #value for a
    a = input("Please enter a value for a: ")
    while isNum(a) != True:
        print("")
        print("Please enter a numeric value")
        a = input("Please enter a value for a: ")

    #value for b
    print("")
    b = input("Please enter a value for b: ")
    while isNum(b) != True:
        print("")
        print("Please enter a numeric value")
        b = input("Please enter a value for b: ")

    a = int(a)
    b = int(b)
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    print(f"A triangle, given leg \"a\" as {a} and leg \"b\" as {b} will result in the hypotenuse being being {c}")

optionsA = {
    "a": getA,
    "b": getB,
    "c": getC
}

optionsA[typeVar]()