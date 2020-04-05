from nltk.corpus import verbnet as vn
from nltk.corpus import wordnet as wn


class verbnet_synset(object):
    def __init__(self, classid):
        self.classid = classid
        
    def __repr__(self):
        return "Classid_" + str(self.classid)
    
    def hyponyms(self):
        """
        Causion: WordNet's hyponym is different from VerbNet's subclass.
        This code imitates WordNet's Synset.
        """
        try:
            subclasses = vn.subclasses(self.classid)
            return [verbnet_synset(subclass)
                    for subclass in subclasses]
        except:
            return []
    
    def hypernyms(self):
        """
        Causion: WordNet's hypernym is different from VerbNet's superclass.
        This code imitates WordNet's Synset.
        """
        if len(self.classid.split("-")) <= 2:
            return []
        return [verbnet_synset("-".join(self.classid.split("-")[:-1]))]
    
    def lemmas(self):
        return vn.lemmas(vn.vnclass(self.classid))
    
    def get_wordnetids(self):
        wordnetids = []
        for synsetid in vn.wordnetids(self.classid):
            if "?" in synsetid:
                # ?propose%2:32:00:: in WordNet. I don't know why ????
                continue
            if len(synsetid.split(":")) == 5:
                wordnetids.append(wn.lemma_from_key(synsetid).synset())
            else:
                wordnetids.append(wn.lemma_from_key(synsetid+"::").synset())
        return wordnetids
    

class verbnet_interface(object):
    def __init__(self, word):
        self.word = word
        self.synsets = [verbnet_synset(classid) for classid in vn.classids(word)]
        
    def __repr__(self):
        return "Verb_" + str(self.word)