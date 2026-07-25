class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l=[]
        x=s1.split()+s2.split()
        c=Counter(x)
        for word,freq in c.items():
            if freq==1 :
                l.append(word)
        
        return l
