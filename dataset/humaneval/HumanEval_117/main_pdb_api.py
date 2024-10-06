from typing import *	##line:(1)
def select_words(s, n):	##line:(2)
    result = []	##line:(3)
    for word in s.split():	##line:(4)
        n_consonants = 0	##line:(5)
        for i in range(0, len(word)):	##line:(6)
            if word[i].lower() not in ["a","e","i","o","u"]:	##line:(7)
                n_consonants += 1 	##line:(8)
        if n_consonants == n:	##line:(9)
            result.append(word)	##line:(10)
    return result	##line:(11)
	##line:(12)

select_words("Mary had a little lamb", 4) 