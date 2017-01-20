# module for wordfrequency calculations, taken from: http://programminghistorian.org/lessons/counting-frequencies

stopwords = []
# Danish
# http://www.ranks.nl/stopwords/danish
# https://github.com/ekorn/Keywords/blob/master/stopwords/danish-stopwords.txt

# English
# http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words


# Given a list of words, return a dictionary of
# word-frequency pairs.

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))
    
    
# Sort a dictionary of word-frequency pairs in
# order of descending frequency.

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux
    
    
# Given a list of words, remove any that are
# in a list of stop words.

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]