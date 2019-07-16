import nltk,itertools

'''
Handout 4
NAME:  Hemanth Kumar Battula

'''

def sentence_segmentation(raw_text):
    return nltk.sent_tokenize(raw_text)

def word_tokenization(raw_text):
    return nltk.word_tokenize(raw_text)

def compute_tags_stats(tagged_words):
    noun_count=len([y for (x,y) in tagged_words if y in ['NN','NNP','NNPS','NNS']])
    verb_count=len([y for (x,y) in tagged_words if y in ['VB','VBD','VBG','VBN','VBZ','VBP' ]])
    adj_count=len([y for (x,y) in tagged_words if y in ['JJ','JJR','JJS']])
    return (noun_count,verb_count,adj_count)

def print_corpus_stats(sentences,words):
    print("="*50)
    print('{:>30}'.format("Corpus Stats\n"))
    print("Number of Sentences: "'{:>10}'.format(len(sentences)))
    print("Number of words: "'{:>14}'.format(len(words)))
    print("="*50)

def print_tags_stats(nr_nouns,nr_verbs,nr_adjs):
    print("="*50)
    print('{:>30}'.format("Tags Stats\n"))
    print("Number of Nouns: "'{:>20}'.format(nr_nouns))
    print("Number of Verbs: "'{:>20}'.format(nr_verbs))
    print("Number of Adjectives: "'{:>15}'.format(nr_adjs))
    print("="*50)

def tag_and_print_text(taggers,words):

    for tagger in taggers:
        tagged_words=tagger.tag(words)
        (noun_count,verb_count,adj_count)=compute_tags_stats(tagged_words)
        print_tags_stats(noun_count,verb_count,adj_count)

def compare_taggers(taggers,words):
        gold_standard=taggers[4].tag(words)
        for tagger in taggers[0:4]:
            count=0
            new_tag=tagger.tag(words)
            print("score for ",tagger, "with respect to gold standard:",len([x for x,y in zip(gold_standard,new_tag) if x==y])/len(gold_standard))


def train_nltk_taggers():
    """this function returns five taggers """
    train_sents = brown_tagged_sents = nltk.corpus.brown.tagged_sents(categories='news')
    default_tag = most_common_tag(train_sents)
    default_tagger = nltk.DefaultTagger(default_tag)
    affix_tagger = nltk.AffixTagger(train_sents,backoff=default_tagger)
    unigram_tagger = nltk.UnigramTagger(train_sents,backoff=affix_tagger)
    bigram_tagger = nltk.BigramTagger(train_sents,backoff=unigram_tagger)
    trigram_tagger = nltk.TrigramTagger(train_sents,backoff=bigram_tagger)
    return [default_tagger,affix_tagger,unigram_tagger,bigram_tagger,trigram_tagger]


def most_common_tag(train_sents):
    """ it returns most common tag, which is then used as default tag"""
    tags = [tag for (token,tag) in list(itertools.chain.from_iterable(train_sents))]
    fdist = nltk.FreqDist(tags)
    (tag,n) = fdist.most_common(1)[0]
    return tag

if __name__ == "__main__":
    raw_text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
    sentences = sentence_segmentation(raw_text)
    words = word_tokenization(raw_text)
    print_corpus_stats(sentences,words)
    taggers = train_nltk_taggers()
    tag_and_print_text(taggers,words)
    compare_taggers(taggers,words)

