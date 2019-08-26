# Levenshtein (minimum) distance between 2 strings
# Coded following Skiena recursive algorithm and adding memoization
# 08/25/2019
class Levenshtein:
    def minDistance(self, word1: str, word2: str) -> int:
        def wordmatch (s1,s2):
            if s1==s2:
                return 0
            else:
                return 1
        def helper(word1,word2,i,j):
            if memo[i][j]:
                return memo[i][j]
            if not word1:
                memo[i][j] = len(word2)
                return memo[i][j]
            if not word2:
                memo[i][j] = len(word1)
                return memo[i][j]
            lower_cost = float('inf')
            match = helper(word1[:i],word2[:j],i-1,j-1)+\
                           wordmatch(word1[-1],word2[-1])
            insert = helper(word1[:], word2[:j],i,j-1)+1
            delete = helper(word1[:i], word2[:],i-1,j)+1
            memo[i][j] = min(match,insert,delete)
            return memo[i][j]

        memo = [[None for _ in range(len(word2)+1)] \
                for _ in range(len(word1)+1)]
        if not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        else:
            return helper(word1,word2,len(word1)-1, len(word2)-1)


if __name__=="__main__":
    lev = Levenshtein()
    while True:
        word1 = input("word1: ")
        word2 = input("word2: ")
        print(lev.minDistance(word1, word2))
