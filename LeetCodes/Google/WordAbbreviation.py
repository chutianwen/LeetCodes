'''
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word
following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of
only the first character until making the map from word to abbreviation become unique. In other words, a final
 abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
'''
import collections
class Solution(object):
    def wordsAbbreviation(self, A):
        '''
        Call two words similar if they have the same first letter, last letter, and length. Only words that are similar
        are eligible to have the same abbreviation. This motivates us to group words by similarity (it is an equivalence
        relation.)

        For each group G of similar words, consider a word W. If it has a longest common prefix P with any other word
        X in G, then our abbreviation must contain a prefix of more than |P| characters. Sort G. It must be the case
        that the longest common prefix of W with any other word X in G must occur with words adjacent to W, so we
        only need to check those.
        :param A:
        :return:
        '''
        def wordsAbbreviation(self, A):
            def longest_common_prefix(a, b):
                i = 0
                while i < len(a) and i < len(b) and a[i] == b[i]:
                    i += 1
                return i

            ans = [None for _ in A]

            groups = collections.defaultdict(list)
            for index, word in enumerate(A):
                groups[len(word), word[0], word[-1]].append((word, index))

            for (size, first, last), enum_words in groups.iteritems():
                enum_words.sort()
                lcp = [0] * len(enum_words)
                for i, (word, _) in enumerate(enum_words):
                    if i:
                        word2, _ = enum_words[i-1]
                        p = longest_common_prefix(word, word2)
                        lcp[i] = max(lcp[i], p)
                        lcp[i-1] = max(lcp[i-1], p)

                for (word, index), p in zip(enum_words, lcp):
                    delta = size - 2 - p
                    if delta <= max(1, len(str(delta)) - 1):
                        ans[index] = word
                    else:
                        ans[index] = word[:p+1] + str(delta) + last

            return ans