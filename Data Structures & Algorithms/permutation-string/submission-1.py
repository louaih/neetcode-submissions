class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perms = permutations(s1)
        print(perms)
        for p in perms:
            if "".join(p) in s2:
                return True
        return False