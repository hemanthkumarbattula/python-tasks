""" Module Text Classification

 Final assignment of LT2111/LT2001 HT2018

Hemanth Kumar Battula
MLT
University of Gothenburg

"""

import math
import nltk
import csv
from fa_aux import *
from nltk.metrics import ConfusionMatrix


def dot_product(p1, p2):
    '''Calculates the dot product of two profiles
    :param p1:
        Dictionary  with keys(integers) and values(floats or integers)
    :param p2:
        Dictionary  with keys(integers) and values(floats or integers)
    :return:
        float
        Dot product of two profiles
    '''
    return sum([p1[i] * p2[i] for i in p1.keys() if i in p2.keys()])


def cosine_similarity(p1, p2):
    '''Calculates cosine similarity of two profiles
    :param p1:
        Dictionary  with keys(integers) and values(floats or integers)
    :param p2:
        Dictionary  with keys(integers) and values(floats or integers)
    :return:
        float
        Cosine similarty 0<= value <= 1 .
    '''
    return (dot_product(p1, p2)) / ((math.sqrt(dot_product(p1, p1))) * (math.sqrt(dot_product(p2, p2))))


def split_data():
    '''Splits the data in Brown corpus data into test collection and reference collection based on test count provided
    :return:
        List of tuples
        Test collection which is a list of tuples(pairs of genre,list of words) of length 56
    :return:
        Dictionary
        Reference collection which is a dictionary of key value pairs(genre,concatenation of list of words)
            of length 15
    '''
    test_collection = []
    ref_collections = {}
    categorys = nltk.corpus.brown.categories()
    reserved_file_count = {"adventure": 3, "belles_lettres": 8, "editorial": 3, "fiction": 3,
                           "government": 4, "hobbies": 4, "humor":1, "learned":9, "lore":5,
                           "mystery":3, "news":5, "religion":2, "reviews":2, "romance": 3, "science_fiction":1}
    for i in categorys:
        x = nltk.corpus.brown.fileids([i])
        for count,j in enumerate(x, start = 1):
            if count <= reserved_file_count[i]:
                text = nltk.corpus.brown.tagged_words(j)
                tokens=[word if 'NP' in tag else word.lower() for word,tag in text]
                test_collection.append((i, tokens))
            else:
                text = nltk.corpus.brown.tagged_words(j)
                tokens=[word if 'NP' in tag else word.lower() for word,tag in text]
                if i in ref_collections.keys():
                    ref_collections[i] +=tokens
                else:
                    ref_collections[i] = tokens
    return test_collection, ref_collections

def read_tsv():
    '''Read brown corpus frequencies from a tab separated file
    :return:
        Dictionary
        A dictionary of word:relative_frequency by reading a file with tab separated key,value pairs


    '''
    try:
        with open('brown_freqs.tsv') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            return {row[0]: float(row[1]) for row in reader}
    except FileNotFoundError as f:
        print(f)
        exit(1)

def modal_profile(text):
    '''Calculate modal profile for a list of tokens

    :param text:
        List of words
    :return:
        Dictionary
        modal profile of type dictionary with keys as the verbs and
        values as the relative frequency of verbs in text
    '''

    return {i: text.count(i)/len(text) for i in ['can', 'could', 'may', 'might', 'must', 'will']
            if i in text}



def topn_profile(text, n, corpus_freqs):
    '''calculate topn profile for a list of tokens considering top n words of corpus_freqs
    :param text:
        list of tokens
    :param n:
        integer
    :param corpus_freqs:
        Dictionary with word:frequency of total brown corpus
    :return:
        dictionary
        mapping top n words in corpus_freqs that are in text to their relative frequencies in text
    '''
    #Used stack overflow examples to create this sorted list
    s = sorted(corpus_freqs.items(), key=lambda k:k[1], reverse=True)[:n]
    return {k[0]: text.count(k[0]) / len(text)
            for k in s if k[0] in text}

def ztopn_profile(text, n, corpus_freqs):
    '''calculate ztopn profile for a list of tokens considering top n words of corpus_freqs
    :param text:
        list of tokens
    :param n:
        integer
    :param corpus_freqs:
        Dictionary with word:frequency of total brown corpus
    :return:
        dictionary
        mapping top n words in corpus_freqs that are in text to their zscores
    '''
    #Used stack overflow examples to create this sorted list
    s = sorted(corpus_freqs.items(), key=lambda k:k[1], reverse=True)[:n]
    return {k[0]: zscore(text.count(k[0]), len(text), corpus_freqs[k[0]])
            for k in s if k[0] in text}


def get_modal_profile_accuracy(test, ref):
    '''creates list of lists with cosine similarities of all 56 tests with 15 references
       The total length of list is 56 and each list is of length 15 having cosine similarities of a test w.r.t reference
    :param test:
        Test Collection
    :param ref:
        Reeference collection
    :return:
        List of lists, List
        List of lists with all cosine similarities of 56 tests w.r.t 15 refernces
        A reference matrix with actual category of each test
    '''
    cs_list = []
    ref_matrix = []
    for k,v in test:
        text_class = []
        test_modal_profile = modal_profile(v)
        for i,j in ref.items():
            ref_modal_profile = modal_profile(j)
            cs= cosine_similarity(test_modal_profile, ref_modal_profile)
            text_class.append((i, cs))
        #Used stack overflow examples to create this sorted list
        sorted_list = [(i, j) for i, j in sorted(text_class, key=lambda x: x[1], reverse=True)]
        ref_matrix.append(k)
        cs_list.append(sorted_list)
    return cs_list,ref_matrix


def get_topn_profile_accuracy(test, ref, n, corpus_freqs):
    '''creates list of lists with cosine similarities of all 56 tests with 15 references
       The total length of list is 56 and each list is of length 15 having cosine similarities of a test w.r.t reference
    :param test:
        Test Collection
    :param ref:
        Reeference collection
    :param n:
        integer
    :param corpus_freqs:
            Dictionary with word:frequency of total brown corpus
    :return:
        List of lists, List
        List of lists with all cosine similarities of 56 tests w.r.t 15 references
        A reference matrix with actual category of each test
    '''
    ref_matrix = []
    cs_list = []
    for k,v in test:
        text_class = []
        test_topn_profile = topn_profile(v, n, corpus_freqs)
        for i,j in ref.items():
            ref_topn_profile = topn_profile(j, n, corpus_freqs)
            cs = cosine_similarity(test_topn_profile, ref_topn_profile)
            text_class.append((i,cs))
        #Used stack overflow examples to create this sorted list
        sorted_list = [(i, j) for i, j in sorted(text_class, key=lambda x: x[1], reverse=True)]
        ref_matrix.append(k)
        cs_list.append(sorted_list)
    return cs_list,ref_matrix


def get_ztopn_profile_accuracy(test, ref, n, corpus_freqs):
    '''creates list of lists with cosine similarities of all 56 tests with 15 references
       The total length of list is 56 and each list is of length 15 having cosine similarities of a test w.r.t reference
    :param test:
        Test Collection
    :param ref:
        Reeference collection
    :param n:
        integer
    :param corpus_freqs:
            Dictionary with word:frequency of total brown corpus
    :return:
        List of lists, List
        List of lists with all cosine similarities of 56 tests w.r.t 15 references
        A reference matrix with actual category of each test
    '''
    cs_list = []
    ref_matrix = []
    for k, v in test:
        text_class = []
        test_ztopn_profile = ztopn_profile(v, n, corpus_freqs)
        for i, j in ref.items():
            ref_ztopn_profile=ztopn_profile(j, n, corpus_freqs)
            cs = cosine_similarity(test_ztopn_profile, ref_ztopn_profile)
            text_class.append((i,cs))
        #Used stack overflow examples to create this sorted list
        sorted_list = [(i, j) for i, j in sorted(text_class, key=lambda x: x[1], reverse = True)]
        ref_matrix.append(k)
        cs_list.append(sorted_list)
    return cs_list,ref_matrix


def print_accuracy(cs_list, ref_matrix, Rank, name):
    '''Prints accuracy of the profiles and creates predicted matrix to print confusion matrices
    :param cs_list:
        List of lists with cosine similarities
    :param ref_matrix:
        A list with actual genres
    :param Rank:
        integer
            The number of top cosine similarities to be considered
    :param name:
        string
        Name of the profile
    :return:
        None
        Prints accuracy and match count and call print confusion matrix function
    '''

    predicted_matrix = []
    accuracy = 0
    for test_count,genre in enumerate(ref_matrix):
        predicted_matrix.append(cs_list[test_count][0][0])
        if genre in [i[0] for i in cs_list[test_count][:Rank]]:
                accuracy += 1
                predicted_matrix[-1] = genre
    match_count="Total Genre Match count={0}".format(str(accuracy))
    print(match_count)
    accuracy_percentage="{2} accuracy for rank {0} is {1}%".format(Rank,math.ceil((accuracy/56)*100 ),name )
    print(accuracy_percentage)
    print_ConfusionMatrix(ref_matrix, predicted_matrix)


def print_ConfusionMatrix(ref, predicted):
    '''Prints confusion matrix with reference as row and predicted as column
    :param ref:
        List of actual genres of tests
    :param predicted:
        List of predicted genres of tests
    :return:
        None
        prints a confusion matrix
    '''
    cm = ConfusionMatrix(ref, predicted)
    Conf_mat = cm.pretty_format(sort_by_count = False, truncate = 15)
    print(Conf_mat)


def main():
    '''Prints all the results of accuracy for modal profile, topn profile, ztopn profile
    Calls all the functions with in the module to print results
    :return:
        None
    '''

    test_collection, ref_collections = split_data()
    corpus_freqs = read_tsv()
    m_cs_list, m_ref_matrix=get_modal_profile_accuracy(test_collection, ref_collections)

    #The below list prints for rank=1 and rank=5. Changing it to range can do for each rank as well
    for i in [1, 5]:
        print("="*15,"MODAL PROFILE for RANK",i, "="*15)
        print_accuracy(m_cs_list, m_ref_matrix, i, "Modal profile")
        print("="*55)

    for n in [20,50,200,500]:
        t_cs_list, t_ref_matrix = get_topn_profile_accuracy(test_collection, ref_collections, n, corpus_freqs)
        z_cs_list, z_ref_matrix = get_ztopn_profile_accuracy(test_collection, ref_collections, n, corpus_freqs)

        #The below list prints for rank=1 and rank=5. Changing it to range can do for each rank as well
        #example: for i in range((1,6): will print accuracies for ranks 1 to 5
        for i in [1, 5]:
            print("="*15, "TOPN PROFILE for RANK", i, "and word count", n, "="*15)
            print_accuracy(t_cs_list, t_ref_matrix, i, "Topn Profile")
            print("="*72)
            print("="*15, "ZTOPN PROFILE for RANK", i, "and word count", n, "="*15)
            print_accuracy(z_cs_list, z_ref_matrix, i, "Ztopn Profile")
            print("="*72)


if __name__ == "__main__":
    main()
