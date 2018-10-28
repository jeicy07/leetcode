class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        from collections import Counter
        
        eleNum = Counter(A)
        num1 = eleNum[1]        # number of 1
        num0 = eleNum[0]        # number of 0
        
        if S > num1:
            return 0
        else:
            one = [ a for a in range(len(A)) if A[a] == 1]    # index of "1"
            zero = []                                         # number of "0" beside each "1"
            if one is None:
                zero.append(len(A))
            elif S == 0 and not num1:          # A:all 0; S: 0          
                    return num0 * (num0 + 1) / 2
            else:
                tmp = one[1:]
                tmp.append(len(A))
                tmp = [tmp[i] - one[i] - 1 for i in range(len(tmp))]
                zero.append(one[0])
                for i in tmp:
                    zero.append(i)

            if S == 0 and num1:                 # A: not all 0; S: 0
                cnt = 0
                print zero
                for num00 in zero:
                    cnt += num00 * (num00 + 1) / 2
                return cnt
            elif not num0:               # A:all 1; S: not 0
                return len(A) - S + 1
            else:                        # A:both 1 and 0; S: not 0
                cnt = num1 - S + 1
                while i < len(zero) - S:
                    cnt += zero[i] 
                    cnt += zero[i] * zero[i+S]
                    i += 1
                cnt += zero[-1]
                return cnt

#**************discussion*********#
def numSubarraysWithSum(self, A, S):
        c = collections.Counter({0: 1})      # create a counter for hashmap
        psum = res = 0
        for i in A:
            psum += i
            res += c[psum - S]            # if (psum - S) is not in hashmap, return 0
            c[psum] += 1
        return res

# print result:
# >>> A = [1,0,0,1,0,1]
# >>> S = 2
# ('psum:%s, res:%s, c:%s', 1, 0, Counter({0: 1, 1: 1}))
# ('psum:%s, res:%s, c:%s', 1, 0, Counter({1: 2, 0: 1}))
# ('psum:%s, res:%s, c:%s', 1, 0, Counter({1: 3, 0: 1}))
# ('psum:%s, res:%s, c:%s', 2, 1, Counter({1: 3, 0: 1, 2: 1}))
# ('psum:%s, res:%s, c:%s', 2, 2, Counter({1: 3, 2: 2, 0: 1}))
# ('psum:%s, res:%s, c:%s', 3, 5, Counter({1: 3, 2: 2, 0: 1, 3: 1}))               