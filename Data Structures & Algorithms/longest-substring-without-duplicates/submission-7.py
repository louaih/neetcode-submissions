class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = set()

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                print(i, j)
                if len(set(sub)) == len(sub):
                    subs.add(sub)

        print(subs)
        max_len = 0
        for s in subs:
            curr_len = len(s)
            if curr_len > max_len:
                max_len = curr_len

        return max_len

        