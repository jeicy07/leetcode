class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = []
        cnt = 0
        for email in emails:
            i = 0
            while i < len(email):
                if email[i] == '.':
                    email = email[:i] + email[i+1:]
                elif email[i] == '+':
                    atpos = email.find("@")
                    email = email[:i] + email[atpos:]
                    break
                i += 1
            if email not in res:
                res.append(email)
                cnt += 1
        
        return cnt