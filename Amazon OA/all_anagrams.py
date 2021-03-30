# https://leetcode.com/discuss/interview-question/1092392/Amazon-SDE-2-interview-question-(ANAGRAMS)

from collections import defaultdict
class Solution:
    def substringAnagrams(self, s):
        anagrams = defaultdict(set)

        # generate all substrings of s
        for start in range(len(s)):
            for end in range(start, len(s)):
                substring = s[start : end + 1]
                anagrams[''.join(sorted(substring))].add(substring)

        res = []
        for anagramSet in anagrams.values():
            # only extract substrings that have anagrams
            if len(anagramSet) > 1:
                res.extend(list(anagramSet))

        return sorted(res, key = lambda x : (len(x), x))

S = Solution()
print(S.substringAnagrams('abccba'))