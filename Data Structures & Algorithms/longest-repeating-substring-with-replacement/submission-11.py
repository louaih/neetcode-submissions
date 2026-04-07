class Solution:  
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            count = Counter()
            max_freq = 0

            for j in range(i, n):
                count[s[j]] += 1
                max_freq = max(max_freq, count[s[j]])

                if (j - i + 1) - max_freq <= k:
                    max_len = max(max_len, j - i + 1)

        return max_len



        