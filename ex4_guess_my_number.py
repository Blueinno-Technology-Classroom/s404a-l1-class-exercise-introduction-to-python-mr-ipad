import random

ans=random.randint(1,100)
while True:
    num=int(input("Enter a number:"))
    print(f"you number is {num}")
    if ans==num:
        print("You are correct")
        break
    elif ans<num:
        print("You are too large")
    else:
        print("You are too small")