class Solution:
    def sortedCount(self,N,M,Mat):
        #code here
        count = 0
        for i in range(N):
            test_list = Mat[i]
            res1 = all(i < j for i, j in zip(test_list, test_list[1:]))
            res2 = all(i > j for i, j in zip(test_list, test_list[1:]))
            if(res1 or res2):
                count += 1
        return count
