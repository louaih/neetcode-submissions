class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = [0 for _ in range(26)]
        c2 = [0 for _ in range(26)]

        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1

        left = 0
        right = len(s1) - 1

        while right < len(s2):
            c2 = [0 for _ in range(26)]
            for i in range(left, right+1):
                c2[ord(s2[i]) - ord('a')] += 1

            print(c1, c2)
            if c1 == c2:
                return True
            left += 1
            right += 1

        return False



        