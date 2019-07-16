import nltk
import re
import difflib

name="""Lab 1: WordNet (deadline: 2018-11-27)
Name : HEMANTH KUMAR BATTULA
Course: MLT
"""


def get_corpus_text(nr_files=199):
    """Returns the raw corpus as a long string.
    'nr_files' says how much of the corpus is returned;
    default is 199, which is the whole corpus.
    """
    fileids = nltk.corpus.treebank_raw.fileids()[:nr_files]
    corpus_text = nltk.corpus.treebank_raw.raw(fileids)
    # Get rid of the ".START" text in the beginning of each file:
    corpus_text = corpus_text.replace(".START", "")
    return corpus_text


def fix_treebank_tokens(tokens):
    """Replace tokens so that they are similar to the raw corpus text."""
    return [token.replace("''", '"').replace("``", '"').replace(r"\/", "/")
            for token in tokens]


def get_gold_tokens(nr_files=199):
    """Returns the gold corpus as a list of strings.
    'nr_files' says how much of the corpus is returned;
    default is 199, which is the whole corpus.
    """
    fileids = nltk.corpus.treebank_chunk.fileids()[:nr_files]
    gold_tokens = nltk.corpus.treebank_chunk.words(fileids)
    return fix_treebank_tokens(gold_tokens)


def tokenize_corpus(text):
    """

    :param text: takes raw text as input
    :return:
        type list
        Returns a list of words(tokens) that matches the regular expression.
    """
    #If few of the text corpus words are hard coded we can achieve even more f-score

    pattern=re.compile("\d+[,\d]%?\-\w[-\w]\w+|\d+,+\d[,\d]*\d+|\d+\/\d+" +
        "|\d+[\.:]\d+|\w{2,}\-\w*[\-\w]*\w+|\w+&\w+|\d+(?=\.[^0-1]+)|" +
        "\w{4,}(?=\.)|[A-Za-z]+/[A-Za-z]+|\w+(?=n't)|n't|\w+(?=')|[\w\.-]+|" +
        "'\w+|\w+|[\.]$|[\w]+[\.][\w][\.]|[A-Z\-\']{2,}(?![a-z])|[A-Z\-\']" +
        "[a-z\-\']+(?=[A-Z])|[\'\w\-]+(?=\.)|[][!&#,;\"'?():-_`$}{%]")
    tokens=re.findall(pattern,text)
    return tokens


def evaluate_tokenization(test_tokens, gold_tokens):
    """Finds the chunks where test_tokens differs from gold_tokens.
    Prints the errors and calculates similarity measures.
    """
    matcher = difflib.SequenceMatcher()
    matcher.set_seqs(test_tokens, gold_tokens)
    error_chunks = true_positives = false_positives = false_negatives = 0
    print(" Token%30s  |  %-30sToken" % ("Error", "Correct"))
    print("-" * 38 + "+" + "-" * 38)
    for difftype, test_from, test_to, gold_from, gold_to in matcher.get_opcodes():
        if difftype == "equal":
            true_positives += test_to - test_from
        else:
            false_positives += test_to - test_from
            false_negatives += gold_to - gold_from
            error_chunks += 1
            test_chunk = " ".join(test_tokens[test_from:test_to])
            gold_chunk = " ".join(gold_tokens[gold_from:gold_to])
            print("%6d%30s  |  %-30s%d" % (test_from, test_chunk, gold_chunk, gold_from))
    precision = 1.0 * true_positives / (true_positives + false_positives)
    recall = 1.0 * true_positives / (true_positives + false_negatives)
    fscore = 2.0 * precision * recall / (precision + recall)
    print()
    print("Test size: %5d tokens" % len(test_tokens))
    print("Gold size: %5d tokens" % len(gold_tokens))
    print("Nr errors: %5d chunks" % error_chunks)
    print("Precision: %5.2f %%" % (100 * precision))
    print("Recall:    %5.2f %%" % (100 * recall))
    print("F-score:   %5.2f %%" % (100 * fscore))
    print()


def number_of_word_tokens(t):
    '''

    :param t: List of tokens
    :return:
        type int
        Returns length of a list
    '''
    return len(t)


def number_of_word_types(t):
    '''

    :param t:List of tokens
    :return:
        :type int
        Returns total word types in list
    '''
    freq= nltk.FreqDist(tokens)
    return len([k for k in freq.keys()])


def average_word_token_length(tokens):
    '''

    :param t:List of tokens
    :return:
        :type float
        Returns value with average word length in corpus
    '''
    freq= nltk.FreqDist(tokens)
    return (sum([len(k) for k in tokens])/ len(tokens))


def longest_word_length(tokens):
    '''

    :param t:List of tokens
    :return:
        :type int
        Returns maximum length word in the list
    '''
    return   max(len(word) for word in tokens)


def words_with_longest_length(tokens):
    '''

    :param t:List of tokens
    :return:
        :type int
        Returns list of words with longest length in list
    '''
    maxlen= max(len(word) for word in tokens)
    return [word for word in tokens if len(word) == maxlen]


def number_of_hapax_words(tokens):
    '''

    :param t:List of tokens
    :return:
        :type int
        Returns total number of hapax words in list
    '''
    freq= nltk.FreqDist(tokens)
    return len(freq.hapaxes())


def percent_of_hapax_words(tokens):
    '''

    :param t:List of tokens
    :return:
        :type float
        Returns percentage of hapax words  in list
    '''
    freq= nltk.FreqDist(tokens)
    return (len(freq.hapaxes())/len(tokens))*100


def most_common_words(tokens,n):
    '''

    :param tokens: List of tokens
    :param n: integer n
    :return:
        :type: list
        Returns list of n words that are most common in the list
    '''
    fdist = nltk.FreqDist(tokens)
    most_common=fdist.most_common(n)
    return most_common


def percentage_of_most_common_words(tokens,n):
    '''

    :param tokens: List of tokens
    :param n: integer n
    :return:
        :type: list of tuples
        Returns list tuples with n most common words and their percentages in the list
    '''
    fdist = nltk.FreqDist(tokens)
    most_common=fdist.most_common(10)
    return [(k,v,(v/len(tokens))*100) for k,v in most_common]


def split_list(tokens,n):
    '''

    :param tokens: List of tokens
    :param n: integer n
    :return:
        :type: list of lists
        Returns list of lists split into n almost equal slices from a given list
    '''
    return [tokens[(i*len(tokens))//n:((i+1)*len(tokens))//n] for i in range(n)]


def return_bigrams(text):
    '''

    :param text: List of tokens
    :return:
        :type: int
        Return total number of bigrams formed by list of tokens
    '''
    return len(list(nltk.bigrams(text)))

def unique_bigrams(text):
    '''

    :param text: List of tokens
    :return:
        :type: int
        Return total number of unique bigrams formed by list of tokens
    '''
    return len(set(nltk.bigrams(text)))

def return_trigrams(text):
    '''

    :param text: List of tokens
    :return:
        :type: int
        Return total number of trigrams formed by list of tokens
    '''
    return len(list(nltk.trigrams(text)))


def unique_trigrams(text):
    '''

    :param text: List of tokens
    :return:
        :type: int
        Return total number of unique trigrams formed by list of tokens
    '''
    return len(set(nltk.trigrams(text)))


def corpus_statistics(tokens):
    '''

    :param tokens:List of tokens
    :return:
        type None
        Prints all the statistics based on corpus
    '''
    print('='*45,'PART-2','='*45)
    print('='*100)
    print('='*45,'Question-1','='*45)
    print('='*100)
    print(f"Toatl Number of words: {number_of_word_tokens(tokens)}")
    print(f"Number of word types: { number_of_word_types(tokens)}")

    print('='*45,'Question-2','='*45)
    print('='*100)
    print(f"Average word token length: {(average_word_token_length(tokens))}")

    print('='*45,'Question-3','='*45)
    print('='*100)
    print(f"Longest word length: {longest_word_length(tokens)}")
    print(f"Words with longest length: {words_with_longest_length(tokens)}")

    print('='*45,'Question-4','='*45)
    print('='*100)
    print(f"Number of hapax words {number_of_hapax_words(tokens)}")
    print(f"Percentage of hapax words: {(percent_of_hapax_words(tokens)):.2f}%")

    print('='*45,'Question-5','='*45)
    print('='*100)
    print("Most common words and their percentages in each slice of ten equal slices")
    print('='*100)
    #Repeating the same in below code
    #for count,word in enumerate(most_common_words(tokens,10),start=1):
    #    print(f"The top {count} most common word is '{word[0]}' and is of size '{word[1]}'")

    for count,word in enumerate(percentage_of_most_common_words(tokens,10),start=1):
        print(f"The top {count} most common word is '{word[0]}' of size '{word[1]}'"
              f"and its percentage in the whole corps is'{word[2]:.2f}%'")

    print('='*45,'Question-6','='*45)
    print('='*100)
    print("Hapaxes and their percentages in each slice of ten equal slices")
    print('='*100)
    increment_corpus=[]
    result_percentages=[]
    equal_freq={}
    concatenated_freq ={}
    equal_perc={}
    concatenated_perc ={}
    for count,l in enumerate(split_list(tokens,10),start=1):
        hapax_count= number_of_hapax_words(l)
        individual=percent_of_hapax_words(l)
        print(f"The number of hapaxes of {count} sub corpora "
              f"out of ten equal chunks is {hapax_count}\n")
        print(f"The percentage of hapaxes of {count} sub corpora"
              f" out of ten equal chunks is {(individual):.2f}%\n")
        equal_perc.update({float(hapax_count): float(individual)})
        equal_freq.update({"text"+str(count)+"_"+str(len(l)): float(hapax_count)})

    print('='*45,'Question-6','='*45)
    print('='*100)
    print("Hapaxes and their percentages while incrementing the corpus of ten equal slices")
    print('='*100)
    for count,l in enumerate(split_list(tokens,10),start=1):
        increment_corpus+=l
        hapax_count= number_of_hapax_words(increment_corpus)
        individual=percent_of_hapax_words(increment_corpus)
        print(f"The number of hapaxes of sum of {count} sub corpora "
              f"out of ten equal chunks is {hapax_count}\n")
        print(f"The percentage of hapaxes of sum of {count} "
              f"sub corpora out of ten equal chunks is {(individual):.2f}%\n")
        concatenated_perc.update({float(hapax_count): float(individual)})
        concatenated_freq.update({float(len(increment_corpus)): float(hapax_count)})

    print('='*45,'Question-8','='*45)
    print('='*100)
    print(f"Unique bigrams :{unique_bigrams(tokens)}")
    print(f"Percentage of bigrams: {(unique_bigrams(tokens)/return_bigrams(tokens))*100:.2f}%")

    print('='*45,'Question-9','='*45)
    print('='*100)
    print(f"Unique trigrams: {unique_trigrams(tokens)}")
    print(f"Percentage of unique trigrams:{(unique_trigrams(tokens)/return_trigrams(tokens))*100:.2f}%")

    print('='*45,'Question-7','='*45)
    print('='*100)
    print("close graph to continue execution")
    print("Graph1:Plotting graph with x-axis as hapaxes count and y-axis as percentage in the corpus for equal slices")
    cfd1 = nltk.FreqDist({k:v for k,v in equal_perc.items()})
    cfd1.plot(10,cumulative=False)

    print("close graph to continue execution")
    print("Graph2:Plotting graph with x-axis as length of corpus and y-axis as hapaxes count in the equal slices")
    cfd3 = nltk.FreqDist({k:v for k,v in equal_freq.items()})
    cfd3.plot(10,cumulative=False)

    print("close graph to continue execution")
    print("Graph3:Plotting graph with x-axis as hapaxes count and y-axis as percentage in the corpus for incrementing lists")
    cfd2 = nltk.FreqDist({k:v for k,v in concatenated_perc.items()})
    cfd2.plot(10,cumulative=False )

    print("close graph to continue execution")
    print("Graph4:Plotting graph with x-axis as length of corpus and y-axis as hapaxes count in the incrementing lists")
    cfd4 = nltk.FreqDist({k:v for k,v in concatenated_freq.items()})
    cfd4.plot(10,cumulative=False )


if __name__ == "__main__":
    print(name)
    print('='*45,'PART-1','='*45)
    print('='*100)
    nr_files = 199
    corpus_text = get_corpus_text(nr_files)
    gold_tokens = get_gold_tokens(nr_files)
    tokens = tokenize_corpus(corpus_text)
    evaluate_tokenization(tokens, gold_tokens)
    corpus_statistics(tokens)
