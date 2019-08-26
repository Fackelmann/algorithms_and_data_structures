# Levenshtein

Implementation of algorithm to find Levenshtein distance between 2 strings, using recursion and memoization.

Based on Skiena's [1]

Time complexity O(len(string1)*len(string2))

Space complexity O(len(string1)*len(string2))

Example:

```
word1: hot dog
word2: cute dog
3

word1: ketchup
word2: mustard
7

word1: kitten
word2: sitting
3
```

## References

[1] Steven S. Skiena. 2008. The Algorithm Design Manual (2nd ed.). Springer Publishing Company, Incorporated.
