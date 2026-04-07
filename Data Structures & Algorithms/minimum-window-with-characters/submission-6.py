class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t:
            return s

        tc = Counter(t)

        for window_size in range(len(t), len(s) + 1):
            left = 0
            right = window_size

            while right <= len(s):
                sub = s[left:right]
                sc = Counter(sub)
                if (tc - sc) == Counter():
                    return sub

                left += 1
                right += 1

        return "" 