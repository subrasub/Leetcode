class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        table = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, path):
            if len(path)==len(digits):
                res.append(''.join(path))
                return

            # get the current set of letters
            letters = table[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()

        res = []
        backtrack(0, [])
        return res