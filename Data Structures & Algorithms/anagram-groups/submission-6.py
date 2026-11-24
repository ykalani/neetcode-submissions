from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if anagram : sorted(word) = sorted(word2)
        #need to dynamically create lists 
        #  we have a dict and for each word we add to the dict,  we can 
        #make key: sorted(word)
        # value = list of words 

        grams = defaultdict(list)
        for word in strs: 
            key = tuple(sorted(word))
            grams[key].append(word)

        return list(grams.values())