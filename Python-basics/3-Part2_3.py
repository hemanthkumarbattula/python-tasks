'''
3. A sentence is said to be a pangram if it contains every letter of a given alphabet set at least once. For example the sentence
”We promptly judged antique ivory buckles for the next prize” is a pan-gram for the given alphabet. Write a python function to check whether a string is a pangram or not.

Hint! This can also be solved using the traversal template. Think about what you need to traverse!
'''

def is_pangram(s):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    lst_alpha=list(alphabets)
    for i in lst_alpha[:]:
        if i in s.lower():
            lst_alpha.remove(i)

    if lst_alpha==[]:
        return True
    else:
        return False

def main():
    s=input("Enter a String:")
    if is_pangram(s):
        print("Yes, the string is a pangram")
    else:
        print("No, the string is not a pangram")
main()
