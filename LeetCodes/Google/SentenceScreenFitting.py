'''
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.

'''

class Solution(object):
    '''
    My solution was to preprocess the sentence in order to determine at each index of the sentence how many more words
    can fit in the column. After that I simply iterate through the rows and increment the total word count.
    '''
    def wordsTyping(self, sentence, rows, cols):
        word_nums = self.preprocess(sentence, cols)
        word_count = 0
        for _ in xrange(rows):
            word_count += word_nums[word_count % len(sentence)]
        return word_count/len(sentence)

    # Preprocessing
    def preprocess(self, sentence, cols):
        word_nums = [0] * len(sentence)
        word_ptr, word_sum = 0, 0
        word_len = len(sentence[0])
        for i, word in enumerate(sentence):
            while(word_sum + word_len <= cols):
                word_sum += word_len
                word_ptr += 1
                word_len = len(sentence[word_ptr % len(sentence)]) + 1
            word_nums[i] = word_ptr - i
            word_sum -= (len(word) + 1)
        return word_nums