import nltk

def count_words(text):
    d={}
    for i in text:
       if not i in d:
          d[i] = text.count(i)
    return d

def fraction_dist(numerator_dist,denominator_dist):
    temp_dict={}

    for key in denominator_dist.keys():
        if key in numerator_dist:
            temp_dict[key]=numerator_dist[key]/denominator_dist[key]
        else:
            temp_dict[key]=0

    '''
  I am not sure,(unable to find in the question) how to handle words from the denominator distribution
   that do not occur in the numerator distribution. so just made their ratio zero.
   '''

    for w in sorted(temp_dict, key=temp_dict.get, reverse=False):
        print(temp_dict[w]," ",w)

if __name__ == "__main__":
    alice_text = nltk.corpus.gutenberg.words('carroll-alice.txt')
    deno_dist=count_words([x.lower() for x in alice_text[:len(alice_text)//2] if x.isalpha()])
    nume_dist=count_words([x.lower() for x in alice_text[len(alice_text)//2:] if x.isalpha()])
    fraction_dist(nume_dist,deno_dist)
