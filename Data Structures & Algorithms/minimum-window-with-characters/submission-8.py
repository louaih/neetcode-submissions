class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge cases
        if len(t) > len(s):
            return ""
        if s == t:
            return s

        # sliding window with size increasing after every pass
        tc = Counter(t)
        left = 0
        right_start = len(t)

        while right_start <= len(s):
            left = 0
            right = right_start

            while right <= len(s):
                sub = s[left:right]
                sc = Counter(sub)
                if (tc - sc) == Counter():
                    return sub

                left += 1
                right += 1
            
            right_start += 1
        return ""
            
