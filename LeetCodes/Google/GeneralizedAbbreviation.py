'''
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
'''

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                # Once we reach the end, append current to the result
                result.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, result)
                # Include current position, and zero-out count
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)

        result = []
        helper(word, 0, '', 0, result)
        return result

    def generateAbbreviations1(self, word):
        return [re.sub('#+', lambda m: str(len(m.group())), ''.join(masked))
                for masked in itertools.product(*(c+'#' for c in word))]

    def 2(self, word):
        return [word] + [word[:first] + str(last - first + 1) + word[last+1:last+2] + rest
                         for last in range(len(word))
                         for first in range(last + 1)
                         for rest in self.generateAbbreviations2(word[last+2:])]

    def generateAbbreviations3(self, word):
        return [word] + [word[:begin] + str(end - begin) + word[end:end+1] + rest
                         for begin, end in itertools.combinations(range(len(word)+1), 2)
                         for rest in self.generateAbbreviations3(word[end+1:])]