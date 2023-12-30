

def add_space_to_string(string, wordDict):
    def backtrack(start, path):
        if start == len(string):
            result.append(' '.join(path))
            return
        for end in range(start + 1, len(string) + 1):
            word = string[start:end]
            if word in wordDict:
                backtrack(end, path + [word])
    result = []
    backtrack(0, [])
    return result

# string  = "ilovecatsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog", "i", "love", "il", "ove", "loves","ilove"]
# print(add_space_to_string(string, wordDict))