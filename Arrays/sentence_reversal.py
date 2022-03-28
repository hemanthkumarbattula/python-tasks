def reverse_sentence(s):
    s.strip() #strip the trailing and starting spaces
    words= s.split() # split the sentence to words
    print(' '.join(words[::-1])) # join by reversing the list

def reverse_sentence1(s):
    words = []
    length = len(s)
    spaces = [' ']
    i = 0
    while i < length:
        if s[i] not in spaces:
            word_start= i
            while i < length and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])
        i+=1
    print( ' '.join(reversal(words))) #' '.join(reversed(words))

def reversal(words):
    rev_words = []
    while len(words) > 0 :
        rev_words.append(words.pop())
    return rev_words



reverse_sentence1(' space here ')
reverse_sentence('This is the best')