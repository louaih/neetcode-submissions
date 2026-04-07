class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            if strs[i] == "":
                strs[i] = "µ"

        if not strs:
            return "©"

        return "€".join(strs)


    def decode(self, s: str) -> List[str]:
        if s == "©":
            return []
        words = s.split("€")
        for i in range(len(words)):
            if "µ" in words[i] and len(words[i]) > 1:
                words[i] = words[i].replace("µ", "")
            elif "µ" in words[i] and len(words[i]) == 1:
                print(words[i])
                words[i] = ""
                print(words[i])

        print(words)
        return words


