class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result= []
        for s in strs:
            result.append(str(len(s)))
            result.append(",")
        result.append("#")
        for s in strs:
            result.append(s)
        return ''.join(result)
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        answer = []
        sizes = []
        i = 0
        while s[i] != "#":
            j = i
            while s[j] != ",":
                j +=1
            sizes.append(int(s[i:j]))
            i = j + 1
        
        for size in sizes:
            answer.append(s[i+1: i+size+1])
            i += size
        return answer

