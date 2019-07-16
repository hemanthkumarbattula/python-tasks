a=eval(input("Enter length of stick1:"))
b=eval(input("Enter length of stick2:"))
c=eval(input("Enter length of stick3:"))
if a+b < c or a+c < b or b+c < a :
    print("NO, a Triangle cannot be formed with provided stick lengths")
elif a+b==c or a+c==b or b+c == a:
    print("YES, the sticks of provided length form degenerate triangle")
else:
    print("YES, Can form a triangle with the sticks of provided length",a,b,c)
