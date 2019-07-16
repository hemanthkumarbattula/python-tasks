'''
2. Write a python function to reverse a string which is passed to the function as a parameter. Do not use the built-in reversed function or .reverse method. A sample run is as:

>reverse("1234abcd")
'dcba4321'
Hint! Think about traversing a string character by character and how you would update the return value on each iteration to end up with the reversed string.
'''

def reverse_of_string(s):
    new_string=""
    for i in range(len(s)):
        new_string+=s[-1-i]

    return new_string
def main():
    s=input("Enter a string:")
    print(reverse_of_string(s))
main()
