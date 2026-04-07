class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sorted_strs = [("".join(sorted(strs[i])), i) for i in range(len(strs))]
        indexes = {}

        for i in range(len(sorted_strs)):
            indexes[sorted_strs[i][0]] = indexes.get(sorted_strs[i][0]) + [i] if indexes.get(sorted_strs[i][0]) else [i]
        
        for anagram in indexes.keys():
            cell = []
            for i in indexes[anagram]:
                cell.append(strs[i])
            res.append(cell)

        print(res)

        return res
                
    