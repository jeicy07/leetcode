class Solution(object):
    def totalFruit(self, tree):
        if tree is None or len(tree) == 1 or len(tree) == 2:
            return len(tree)
        else:
            ty1 = ty2 = -1
            mx = tmp = 0
            
            for i in range(0,len(tree)):   
                
                if ty1 == -1:
                    ty1 = tree[i] 
                    tmp = tmp + 1
                elif tree[i] != ty1 and ty2 == -1:
                    ty2 = tree[i]
                    tmp = tmp + 1
                elif tree[i] == ty1 or tree[i] == ty2:
                    tmp  = tmp + 1
                else:
                    mx = tmp if tmp > mx else mx

                    ty1 = tree[i]
                    j = i- 1
                    ty2 = tree[j]
                    tmp = 1
                    
                    while tree[j] == ty1 or tree[j] == ty2:
                        j = j - 1
                        tmp = tmp + 1
                    

                        
                mx = tmp if tmp > mx else mx
        
        return mx
                    
                
                
            
        """
        :type tree: List[int]
        :rtype: int
        """