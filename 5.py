#find leap year or not
y=int(input("enter year"))
if y%4==0:
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")