'''
1. Write a version of the sticks & triangles problem of last weeks assignment, where you use functions to organize your code. Write a) a function called main, that takes no arguments but contains the calls to the other functions and the if-statement with the calls to print, b) a function that asks for three inputs and returns three integers, c) a function that takes three integers and returns True or False depending on whether one of the sticks is longer than the two other combined. You run the whole programme by calling main in your script.

Hint! You can return multiple values in one go from a function by writing

def returns_three_things():
    # something defining a, b and c
    return a, b, c
You can then use a function like this by:

x, y, z = returns_three_things()
'''

def main():
    s1,s2,s3=length_of_sticks()
    if valid_triangle(s1,s2,s3):
        print("Yes")
    else:
        print("No")

def length_of_sticks():
    v1=eval(input("Enter length of stick1:"))
    v2=eval(input("Enter length of stick1:"))
    v3=eval(input("Enter length of stick1:"))
    return v1,v2,v3



def valid_triangle(val1,val2,val3):
    if val1> val2+val3 or val1> val2+val3 or val1> val2+val3:
        return False
    elif val1== val2+val3 or val1== val2+val3 or val1== val2+val3:
        return True
    else:
        return True
main()
