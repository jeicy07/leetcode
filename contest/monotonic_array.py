# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.




class Solution(object):
    def isMonotonic(self, A):
        flag = 0
        cur = 0
        for i in range(len(A)):
            if i == len(A) - 1:
                return True  
            if i != len(A) - 1 and A[i] < A[i+1]:
                if i == len(A) - 2:
                    return True
                else:
                    flag = 0
                    cur = i
                    break
            if i != len(A) - 1 and A[i] > A[i+1]:
                if i == len(A) - 2:
                    return True
                else:
                    flag = 1
                    cur = i
                    break
        
        for j in range(cur,len(A)):
            if flag == 0 and j != len(A) - 1 and A[j] > A[j+1]:
                return False
            if flag == 1 and j != len(A) - 1 and A[j] < A[j+1]:
                return False
            
        return True
                