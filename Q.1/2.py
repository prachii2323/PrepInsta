#Method 1: Using nested-if else
num=int(input("ENter the number: "))
if num>=0:
    if num==0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")