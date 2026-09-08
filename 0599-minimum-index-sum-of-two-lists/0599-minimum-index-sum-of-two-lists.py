class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l=[]
        lsum=0
        minn=float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    lsum=i+j
                    if lsum<minn:
                        minn=lsum
                        l=[list1[i]]
                    elif lsum==minn:
                        l.append(list2[j])
        return l