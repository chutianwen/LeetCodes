'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''
class Solution(object):
	def fullJustify(self, words, maxWidth):
		"""
		:type words: List[str]
		:type maxWidth: int
		:rtype: List[str]
		"""
		# Algorithm: Add as many words as possible to line with
		# spaces in between and increase size of spaces as needed.
		result = []

		word_idx = 0
		while word_idx < len(words):
			next_line = []
			char_count = word_count = space_count = 0

			# Add words and a space while we have words and if there are available characters
			while (
				word_idx < len(words) and
				len(words[word_idx]) <= (maxWidth - (char_count + space_count))
			):
				next_word = words[word_idx]
				next_line.append(next_word)
				next_line.append(" ")
				char_count += len(next_word)
				word_count += 1
				space_count += 1
				word_idx += 1

			# Ignore the last space in our count of valid spaces
			space_count -= 1

			# Get the number of free characters left (not including spaces)
			char_difference = maxWidth - char_count

			# Case 1: if we're out of words or have only
			# one word on the line, then just increase the
			# number of spaces after the last word in the line.
			#
			# The number of spaces added should be the difference
			# in max width and non-space characters less the number
			# of spaces not accounted for in the difference.
			if word_idx == len(words) or word_count == 1:
				next_line[-1] *= (char_difference - space_count)

			# Case 2: otherwise, increase the space size after each
			# character as evenly as possible. Prefer left spaces to
			# apply extra spaces. Drop the last space at the end
			else:
				# pop the last space
				next_line.pop()
				num_spaces, num_slots_with_extra_spaces = divmod(char_difference, space_count)

				# from first space to last - 1
				for space_idx in range(1, word_count+space_count, 2):
					if num_slots_with_extra_spaces:
						next_line[space_idx] *= num_spaces+1
						num_slots_with_extra_spaces -= 1
					else:
						next_line[space_idx] *= num_spaces

			result.append("".join(next_line))
		return result

words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

res = Solution().fullJustify(words, maxWidth)
for row in res:
	print(row)