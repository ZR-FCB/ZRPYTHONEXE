class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        cmp = 0

        while i >= 0:
            if s[i] != ' ':
                cmp += 1
                i -= 1
            else:
                if cmp > 0:
                    return cmp
                i -= 1

        return cmp


           