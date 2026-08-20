class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_order = {}
        for i in range(len(order)):
            char_order[order[i]] = i
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if char_order[w1[j]] > char_order[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True