# Markov chain Monte Carlo cracking of a simple substitution cipher
# Run the code as a scipt to see an example of its use.
#
# Implemented for Intro Programming LT2211 2016 University of Gothenburg
# by Gerlof Bouma

from math import log, exp
from random import seed, choice, random
import math
# mcmc_crack
#
# implements the simplest algorithm from Chen & Rosenthal (2012,
# 'Decrypting classical cipher text using Markov chain Monte Carlo',
# doi:10.1007/s11222-011-9232-5) to crack a substitution cipher
#
# Arguments: encrypted text as string
#            scoring function as function string -> float
#            alphabet as string
# Optionals: number of iterations as integer (default 10000)
#            logging flag as boolean (default False)
#            logging interval as boolean (default 1000)
# Returns: decrypted text as string
#
def mcmc_crack(cipher_text, score_from_lm, abc,
               nr_of_iterations=2000,
               log_progress=False, log_interval=400):

    # 0 Create an initial key
    decryption_key = dict(zip(abc,abc))
    # 1a ...decrypt the text with it
    plain_text = tuple(decryption_key[c] for c in cipher_text)
    # 1b ...and calculate how good the result is
    score = score_from_lm(plain_text)
    
    for iteration in range(nr_of_iterations):

        # Some simple logging to stderr at regular intervals if requested.
        #
        if log_progress and iteration % log_interval == 0:
             print(iteration, score, ''.join(plain_text), file=sys.stderr, end='\n\n')

        # 2 Create a new key with two mappings from the old key
        # swapped
        decryption_key1 = dict(decryption_key)
        a = choice(abc)
        b = choice(abc)
        decryption_key1[a],decryption_key1[b] = decryption_key1[b],decryption_key1[a]

        # 4a ... decrypt th text with the new key
        plain_text1 = tuple(decryption_key1[c] for c in cipher_text)
        # 4b ... and calculate how good the result is
        score1 = score_from_lm(plain_text1)
    
        # 5 Decide whether to go with the new key or to keep the old

        if score1 > score or random() < exp(score1-score):
            score = score1
            plain_text = plain_text1
            decryption_key = decryption_key1

        # Repeat from 2
        
    return score, decryption_key, plain_text


if __name__ == "__main__":
    import sys
    import pickle
    
    # Example run of the cracking function

    # We set the seed of the random number generator, so that 'the
    # same random' result will always be generated. In real
    # applications, you would remove this.
    seed(8)

    # The example problem is defined by a cipher text and an alphabet.
    cipher_text = "axee lvdbugczvxkcelyffyocxipczh ckfyzhgczdw kcpypcogl cxipcoytef cyiczh cvxe cxffctytkgcv l czh cedldodw kcxipczh ctdt clxzhkcdmzolxe ce vxl czh caxee lvdbuctgckdiczh caxvkczhxzceyz czh cbfxvkczhxzcbxzbhce vxl czh cameameceylpcxipckhmiczh crlmtydmkcexip lkixzbhch czdduchykcwdlsxfckvdlpcyichxipcfdioczyt czh ctxindt crd ch ckdmohzckdcl kz pch cegczh czmtzmtczl  cxipckzddpcxvhyf cyiczhdmohzcxipcxkcyicmrrykhczhdmohzch ckzddpczh caxee lvdbucvyzhc g kcdrcrfxt cbxt cvhyrrfyioczhldmohczh czmfo gcvddpcxipcemlef pcxkcyzcbxt cdi czvdcdi czvdcxipczhldmohcxipczhldmohczh cwdlsxfcefxp cv izckiybu lkixbuch cf rzcyzcp xpcxipcvyzhcyzkch xpch cv izcoxfmtshyiocexbucxipchxkzczhdmckfxyiczh caxee lvdbucbdt czdctgcxltkctgce xtykhcedgcdcrlxeadmkcpxgcbxffddhcbxffxgch cbhdlzf pcyichykcadgczvxkcelyffyocxipczh ckfyzhgczdw kcpypcogl cxipcoytef cyiczh cvxe cxffctytkgcv l czh cedldodw kcxipczh ctdt clxzhkcdmzolxe "
    alphabet = 'abcdefghijklmnopqrstuvwxyz '

    # The cracking function expects a score function that will assign a fitness score to a text
    # In this case, the score will be according to an English character bigram model
    with open('lm_dumas_n2.pickle','rb') as f:
        bigram_model = pickle.load(f)

    def score_from_bigram_model(text):
        bigrams = [tuple(text[i:i+2]) for i in range(len(text)-1)]
        return sum(math.log(bigram_model[cc]+1 if cc in bigram_model else 1) for cc in bigrams)

    # Now 
    print('Cipher text:')
    print(cipher_text,end='\n\n')
    
    score,key,plain_text = mcmc_crack(cipher_text,score_from_bigram_model,alphabet,log_progress=True)

    # score, key and plain_text gotten from the mcmc_crack function
    print('Best decryption key:')
    print('[%s]' % (alphabet,))

    print('[%s]' % (''.join(key[c] for c in alphabet),),end='\n\n')

    print('Corresponding plain text:')
    print(''.join(plain_text),end='\n\n')
    
    print('Score according to the language model:')
    print(score)

