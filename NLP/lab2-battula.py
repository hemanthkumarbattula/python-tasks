import nltk
import string
import re
import math


def pre_process(filename):
    '''

    :param filename: Takes text file as input
    :return:
        :type list
        Returns list of sentences
    '''
    file = open(filename, mode='r', encoding="utf8")
    text = file.read()
    file.close()
    # prepare regex for char filtering
    remove_punctuation = re.compile('[%s]+' % re.escape(string.punctuation))
    # remove punctuation from each word
    stripped_text = remove_punctuation.sub('', text)
    # remove numbers and tab spaces
    raw_text = re.sub(r'[0-9]+|\t','', stripped_text)
    #make list of sentences using next line delimeter
    sentences=[s for s in raw_text.split('\n') if s]
    return sentences


def train_language_model(file_path, lang_name):
    '''

    :param file_path: Takes file path of text file
    :param lang_name: language name of text file for training
    :return:
    :type: Dictionary tuples
    Return nested dictionary with details of training texts sentences and n-grams
    Return nested dictionary with probabilities of n-grams
    '''
    train_bigrams=[]
    train_trigrams=[]
    training_details={}
    n_gram_models={}
    #Send file to get raw text and split into sentences based on next line
    sentences=pre_process(file_path)
    #For every sentence calculate bigrams, trigrams and frequency of each n-gram
    for count,sent in enumerate(sentences,start=1):
        words=sent.lower().split()
        tokens=[''.join(ch for ch in w if ch.isalpha())for w in words]
        #test_trigrams=list(nltk.ngrams(tokens, 3)
        #Building trigrams as above would result in undetermined language for a sentence with two words.
        #Adding 'space' as <start> and <end> symbols for a sentence to consider start word and end word for all n-grams
        #This is useful when building n-grams with big n value and small sentences
        train_bigrams+=list(nltk.ngrams(tokens, 2,pad_left=True, pad_right=True, left_pad_symbol=' ', right_pad_symbol= ''))
        train_trigrams+=list(nltk.ngrams(tokens, 3,pad_left=True, pad_right=True, left_pad_symbol=' ', right_pad_symbol= ''))

    bigram_frequency= nltk.FreqDist(train_bigrams)
    trigram_frequency= nltk.FreqDist(train_trigrams)
    lb=len(train_bigrams)
    lt= len(train_trigrams)
    bigram_probability={k:(float(v))/(lb) for k,v in bigram_frequency.items()}
    sorted_bi_prob={k:float(v) for k,v in sorted(bigram_probability.items(), key=lambda item: item[1],reverse=True)}
    trigram_probability= {k:(float(v))/(lt) for k,v in trigram_frequency.items()}
    sorted_tri_prob={k: float(v) for k,v in sorted(trigram_probability.items(), key=lambda item: item[1],reverse=True)}
    training_details.update({lang_name:{"count": count, "len_bigrams":lb,"len_trigrams":lt}})
    n_gram_models.update({lang_name:{"count": count, "len_bigrams":lb,"len_trigrams":lt,"bigram_freq":sorted_bi_prob,
                                     "trigram_freq": sorted_tri_prob}})

    return training_details,n_gram_models

def test_language_model(file_path, lang_name, n_grams_models):
    '''

    :param file_path: Takes file path of test file
    :param lang_name: Actual language name  of the test file
    :param n_grams_models: Dictionary of n-gram models of training data
    :return:
        :type:None
        Prints all the accuracies of test file sentences and detected languages
    '''
    test_results_bi={}
    test_results_tri={}
    sentences=pre_process(file_path)
    len_of_sent=len(sentences)
    bi_undetermined_sentences={}
    tri_undetermined_sentences={}
    for count,sent in enumerate(sentences,start=1):
        words=sent.lower().split()
        tokens=[''.join(ch for ch in w if ch.isalpha())for w in words]
        #Adding 'space' as <start> and <end> symbols for a sentence to consider start word for all n-grams
        #This is useful when building n-grams with big n value and small sentences
        #test_trigrams=list(nltk.ngrams(tokens, 3)
        #Building trigrams as above would result in undetermined language for a sentence with two words.
        test_bigrams=list(nltk.ngrams(tokens, 2,pad_left=True, pad_right=True, left_pad_symbol=' ', right_pad_symbol= ''))
        test_trigrams=list(nltk.ngrams(tokens, 3,pad_left=True, pad_right=True, left_pad_symbol=' ', right_pad_symbol= ''))
        bi_prob=[]
        tri_prob=[]
        for lang in n_grams_models.keys():
            #calculates sum of log of probabilities of bi-grams if present in training bi-grams
            # else considers a small value if bi-gram not present in the training model
            s=sum([math.log(n_grams_models[lang]["bigram_freq"][w],2) if w in  n_grams_models[lang]["bigram_freq"]
                   else math.log(1e-300,2) for w in test_bigrams])

            bi_prob.append((lang,s))
        max_prob=max(bi_prob,key=lambda item:item[1])
        if max_prob[1]!=len(tokens)*math.log(1e-300,2) and max_prob[1]!=0:
            if max_prob[0] in test_results_bi:
                 test_results_bi[max_prob[0]] +=1
            else:
                test_results_bi[max_prob[0]]=1
        if max_prob[0]!=lang_name and max_prob[1]==0:
            bi_undetermined_sentences.update({(lang_name,count):sent})
        for lang in n_grams_models.keys():
            #calculates sum of log of probabilities of tri-grams if present in training tri-grams
            # else considers a small value if tri-gram not present in the training model
            s=sum([math.log(n_grams_models[lang]["trigram_freq"][w],2) if w in  n_grams_models[lang]["trigram_freq"]
                   else math.log(1e-300,2) for w in test_trigrams])
            tri_prob.append((lang,s))
        max_prob=max(tri_prob,key=lambda item:item[1])
        if max_prob[1]!=len(tokens)*math.log(1e-300,2) and max_prob[1]!=0:
            if max_prob[0] in test_results_tri:
                 test_results_tri[max_prob[0]] +=1
            else:
                test_results_tri[max_prob[0]]=1
        if max_prob[0]!=lang_name and max_prob[1]==0:
            tri_undetermined_sentences.update({(lang_name,count):sent})

    print("="*40)
    print(f"Language Name: {lang_name}")
    print("="*40)
    print(f"Total Test sentences in {lang_name} is: {count}")
    print("="*5,"BI-GRAM MODELAS","="*15)
    print(f"Accuracy: {(test_results_bi[lang_name]/count)*100}%")
    print(f"correctly classified: {test_results_bi[lang_name]}")
    print(f"Miss classified: {count-(test_results_bi[lang_name]+len(bi_undetermined_sentences))}")
    print(f"Number of sentences determined: {test_results_bi}")
    print(f"Could not classify: {len(bi_undetermined_sentences)}")
    if bi_undetermined_sentences:
        for lan,s in bi_undetermined_sentences.items():
            print("Actual Language:", lan[0])
            print("Sentence Line Number in test file :", lan[1])
            print("Sentence:", s)

    print("="*5,"TRI-GRAM MODELAS","="*15)
    print(f"Accuracy: {(test_results_tri[lang_name]/count)*100}%")
    print(f"correctly classified: {test_results_tri[lang_name]}")
    print(f"Miss classified: {count-(test_results_tri[lang_name]+len(tri_undetermined_sentences))}")
    print(f"Number of sentences determined: {test_results_tri}")
    print(f"Could not classify: {len(tri_undetermined_sentences)}")
    if tri_undetermined_sentences:
        for lan,s in tri_undetermined_sentences.items():
            print("Actual Language:", lan[0])
            print("Sentence Line Number in test file :", lan[1])
            print("Sentence:", s)
    print("="*40)
    print(f"Total Acuuracy:{(((test_results_bi[lang_name]/count)*100)+((test_results_tri[lang_name]/count)*100))/2}% ")
    print("="*40,"\n")

if __name__ == "__main__":
    lang_name = ["french","english","dutch","italian","german","spanish"]
    lang_path = ["french/french.txt","english/english.txt","dutch/dutch.txt","italian/italian.txt","germany/germany.txt","spanish/spanish.txt"]
    training_details={}
    n_grams_models={}
    print("="*25)
    print(" Corpus Statistics")
    print("="*25)
    for i,file_name in enumerate(lang_path):
        details,models=train_language_model("train/"+file_name, lang_name[i])
        training_details.update(details)
        n_grams_models.update(models)

        print(f"Language Name: {lang_name[i]}")
        print(f'Training sentences: {training_details[lang_name[i]]["count"]}')
        print(f'Number of Bigrams: {training_details[lang_name[i]]["len_bigrams"]}')
        print(f'Number of Trigrams: {training_details[lang_name[i]]["len_trigrams"]}\n')
    print("="*25)
    print(f"Testing Language model")
    print("="*25)
    for i,file_name in enumerate(lang_path):
        test_language_model("test/"+file_name,lang_name[i], n_grams_models)


