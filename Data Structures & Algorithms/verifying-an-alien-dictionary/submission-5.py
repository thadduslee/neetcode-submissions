class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        actual_order = {}
        for index, value in enumerate(order):
            actual_order[value] = index

        for i in range(len(words)-1):
            firstword = words[i]
            secondword = words[i+1]

            for j in range(min(len(firstword), len(secondword))):
                if firstword[j] != secondword[j]:
                    if actual_order[firstword[j]] > actual_order[secondword[j]]:
                        return False
                    break
            else:
                if len(firstword) > len(secondword):
                    return False
        return True

                 
