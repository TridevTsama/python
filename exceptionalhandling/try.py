try:
    num = int(input("enter number"))
    print(10/num)
except zerodivisonerror:
    print("num not be zero")
except valueerror:
    print("invalide input ")
    
    
try:
    num = int(input("enter number"))
    result=10/num
except zerodivisonerror:
    print("num not be zero")
except valueerror:
    print("invalide input ")
else:
    print("result:",result)    
    
    
    
try:
    a=10
    b=0
    print(a/b) 
except:
    print("zero division")       