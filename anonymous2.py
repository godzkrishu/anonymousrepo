a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))
d = int(input("Enter the 4th number: "))

if a >= b and a >= c and a >= d:
    a=10
    print("First number",a,"is the largest")
    if b>a and b>c and b>d:
        print("2nd number",b,"is the largest")
        if c>a and c>b and c>d:
            print("3rd number",c,"is the largest")
        else:
            print("4rth number",d,"is the largest")
            
            
    
