# Write your solution here
num = int(input("How many points [0-100]: "))
if num<0 or num>100:
    print("Grade: impossible!")
elif num<=49:
    print("Grade: fail")
elif num<=59:
    print("Grade: 1")
elif num<=69:
    print("Grade: 2")
elif num<=79:
    print("Grade: 3")
elif num<=89:
    print("Grade: 4")
elif num<=100:
    print("Grade: 5")
