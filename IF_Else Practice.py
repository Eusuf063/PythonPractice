x = float(input())
y = float(input())
z = float(input())

if x > y:
    print("X is greater than Y")
elif x == y:
    print("Both are same")
else:
    print("X is smaller than Y")

print("//////////// else if condition within a line/////////////")

print("X is greater than Y") if x>y else print("Both are equal") if x==y else print("X is smaller than Y")

print("//////////// else if condition with 3 variable with AND logic /////////////")

if x>y and y>z:
    print("Both Condition are true")
else:
    print("Condition doesn't match")

print("//////////// exam grading practice /////////////")

if 90 < x <= 100:
    print("Grade is A")
elif 80 < x <= 90:
    print("Grade is B")
elif 70 < x <= 80:
    print("Grade is C")
elif 55 < x <= 70:
    print("Grade is D")
else:
    print("Congratulation....You have successfully FAILED in the exam")
