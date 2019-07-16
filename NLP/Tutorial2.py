import nltk
import math
def calculate_entropy_unigrams():
    s='''
how much wood would a woodchuck chuck if a woodchuck could chuck wood a \
woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could \
chuck wood 
'''
    tokens=nltk.word_tokenize(s)
    freq= nltk.FreqDist(tokens)
    sum=0
    for i in set(tokens):
        sum+= -(tokens.count(i)/len(tokens))*math.log((tokens.count(i)/len(tokens)),2)
    print("Entropy of unigrams:",sum)

def calculate_entropy_unigrams_smooth():
    s='''
how much wood would a woodchuck chuck if a woodchuck could chuck wood a \
woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could \
chuck wood 
'''
    tokens=nltk.word_tokenize(s)

    freq= nltk.FreqDist(tokens)
    sum=0
    for i in set(tokens):
        prob=(tokens.count(i)+1)/(len(tokens)+len(set(tokens)))
        sum+= (prob)*math.log(prob,2)
    sum=-sum
    print("Entropy of unigrams after smoothing:",sum)

def calculate_entropy_bigrams():
    s='''
start how much wood would a woodchuck chuck if a woodchuck could chuck wood a \
woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could \
chuck wood end
'''
    tokens=nltk.word_tokenize(s)
    big=list(nltk.bigrams(tokens))

    freq= set(big)
    sum=0

    for i in freq:
        num=big.count(i)
        den=tokens.count(i[0])
        prob=num/den

        sum+= (prob)*math.log(prob,2)
    sum=-sum
    print("Entropy of bigrams:",sum)

def calculate_entropy_bigrams_smooth():
    s='''
start how much wood would a woodchuck chuck if a woodchuck could chuck wood a \
woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could \
chuck wood end
'''
    tokens=nltk.word_tokenize(s)
    big=list(nltk.bigrams(tokens))
    len_tokens= len(set(tokens))+1
    freq= set(big)
    sum=0
    for i in freq:
        num=big.count(i)+1
        den=(tokens.count(i[0]))+len_tokens
        prob=num/den

        sum+= (prob)*math.log(prob,2)
    sum=-sum
    print("Entropy of bigrams after smoothing:",sum)

def calperplexity_bigrams1():
        strain='''
        start how much wood would a woodchuck chuck if a woodchuck could chuck wood a \
woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could \
chuck wood end
    '''
        stest="start would a woodchuck chuck wood if it could chuck wood end"
        train_tokens=nltk.word_tokenize(strain)
        V_value=len(set(train_tokens))-1
        test_tokens= nltk.word_tokenize(stest)
        N_value=len(test_tokens)-2

        train_bigrams=list(nltk.bigrams(train_tokens))
        test_bigrams= list(nltk.bigrams(test_tokens))
        product=1
        for i in test_bigrams:

            num=train_bigrams.count(i)+1
            den=test_tokens.count(i[0])+ V_value
            prob=num/den
            product*=prob
        result=product**(-1/N_value)
        print("Perplexity of bigram of sentence 1 over trained corpus is:",result)

def calperplexity_bigrams2():
    #Reference: https://www.coursera.org/learn/language-processing/supplement/fdxeI/perplexity-computation
        strain='''
        start how much wood would a woodchuck chuck if a woodchuck could chuck wood a \
woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could \
chuck wood end
    '''
        stest="start wood a woodchuck chuck would if it could chuck would end"
        train_tokens=nltk.word_tokenize(strain)
        V_value=len(set(train_tokens))-1
        test_tokens= nltk.word_tokenize(stest)
        N_value=len(test_tokens)-2

        train_bigrams=list(nltk.bigrams(train_tokens))
        test_bigrams= list(nltk.bigrams(test_tokens))
        product=1
        for i in test_bigrams:

            num=train_bigrams.count(i)+1
            den=test_tokens.count(i[0])+ V_value
            prob=num/den
            product*=prob
        result=product**(-1/N_value)
        print("Perplexity of bigram of sentence 2 over trained corpus is:",result)

def calperplexity_unigrams1():
        strain='''
        how much wood would a woodchuck chuck if a woodchuck could chuck wood a \
woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could \
chuck wood
    '''
        stest="start would a woodchuck chuck wood if it could chuck wood end"
        train_tokens=nltk.word_tokenize(strain)
        V_value=len(set(train_tokens))
        test_tokens= nltk.word_tokenize(stest)
        N_value=len(test_tokens)
        product=1
        for i in test_tokens:
            num=train_tokens.count(i)+1
            den=len(test_tokens)+ V_value
            prob=num/den
            product*=prob
        result=product**(-1/N_value)
        print("Perplexity of unigram of sentence 1 over trained corpus is:",result)

def calperplexity_unigrams2():
        strain='''
        how much wood would a woodchuck chuck if a woodchuck could chuck wood a \
woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could \
chuck wood
    '''
        stest="wood a woodchuck chuck would if it could chuck would"
        train_tokens=nltk.word_tokenize(strain)
        V_value=len(set(train_tokens))
        test_tokens= nltk.word_tokenize(stest)
        N_value=len(test_tokens)
        product=1
        for i in test_tokens:
            num=train_tokens.count(i)+1
            den=len(test_tokens)+ V_value
            prob=num/den
            product*=prob
        result=product**(-1/N_value)
        print("Perplexity of unigram of sentence 2 over trained corpus is:",result)


def calperplexity_trigrams():
        #Example found from coursera.org
        #Reference: https://www.coursera.org/learn/language-processing/supplement/fdxeI/perplexity-computation
        strain="start start This is the cat that killed the rat that ate the malt that lay in the house that Jack built end"
        stest="start start This is the house that Jack built end"
        train_tokens=nltk.word_tokenize(strain)
        V_value=len(set(train_tokens))-1
        test_tokens= nltk.word_tokenize(stest)
        N_value=len(test_tokens)-3

        train_trigrams=list(nltk.trigrams(train_tokens))
        test_trigrams= list(nltk.trigrams(test_tokens))
        train_bigrams=list(nltk.bigrams(train_tokens))
        test_bigrams= list(nltk.bigrams(test_tokens))
        product=1
        for i in test_trigrams:

            num=train_trigrams.count(i)+1
            den=test_bigrams.count((i[0],i[1]))+ V_value
            prob=num/den
            product*=prob
        result=product**(-1/N_value)
        print(result)

def calculate_prob_bigrams():
    s='start would a woodchuck chuck wood if it could chuck wood end'
    tokens=nltk.word_tokenize(s)
    big=list(nltk.bigrams(tokens))
    print(set(tokens))
    freq= set(big)
    sum=0

    for i in freq:
        num=big.count(i)
        den=tokens.count(i[0])
        prob=num/den
        print(i,prob)
        sum+= (prob)*math.log(prob,2)
    sum=-sum
    print("Entropy of bigrams:",sum)

def calculate_prob_bigrams1():
    s='start wood a woodchuck chuck would if it could chuck would end'
    tokens=nltk.word_tokenize(s)
    big=list(nltk.bigrams(tokens))
    print(set(tokens))
    freq= set(big)
    sum=0

    for i in freq:
        num=big.count(i)
        den=tokens.count(i[0])
        prob=num/den
        print(i,prob)
        sum+= (prob)*math.log(prob,2)
    sum=-sum
    print("Entropy of bigrams:",sum)

calculate_entropy_unigrams()
calculate_entropy_bigrams()
calculate_entropy_unigrams_smooth()
calculate_entropy_bigrams_smooth()
calperplexity_bigrams1()
calperplexity_bigrams2()
calperplexity_unigrams1()
calperplexity_unigrams2()

