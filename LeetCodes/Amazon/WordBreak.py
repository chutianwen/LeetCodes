'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not
contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code
definition to get the latest changes.
'''

from queue import deque
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = filter(lambda x: x in s, wordDict)
        words = set(wordDict)

        def driver(word):
            if word in words:
                return True
            else:
                for i in range(1, len(word)):
                    if word[:i] in words and driver(word[i:]):
                        return True
                return False

        return driver(s)

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = list(filter(lambda x: x in s, wordDict))

        def driver(words, cur, target):
            print(cur)
            if not target.startswith(cur):
                return False
            elif cur == target:
                return True
            else:
                for word in words:
                    if driver(words, cur + word, target):
                        return True
                return False
        return driver(wordDict, '', s)

    def wordbreak3(self, s, wordDict):
        '''
        Dynamic programming
        d[i] is true if s[x:i+1] exist in dict and s[0:x] can be built.
        :param s:
        :param wordDict:
        :return:
        '''
        print(wordDict)
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                print(i-len(w)+1, s[i-len(w)+1:i+1])
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
                    break
        return d[-1]

    def word_break_bfs(self, s, wordDict):
        '''
        O(n^2)
        BFS or DFS. Thinking s as a graph of nodes, each position is a node. The goal is to reaching target(end of s)
        from starting position. Then each word in dictionary is a edge.
        For BFS, from starting node (ix == 0), search its neighbor by checking if s[id_start:id_neighbor] exists in
        wordDict. If such edge exists, means id_neighbor is its neighbor, then push to Q and mark visited
        :param s:
        :param wordDict:
        :return:
        '''
        wordDict = set(filter(lambda x: x in s, wordDict))
        target = len(s)
        visited = set()
        q = deque([0])
        while q:
            cur_index = q.popleft()
            for id in range(cur_index + 1, target + 1):
                if id not in visited:
                    if s[cur_index: id] in wordDict:
                        if id == target:
                            return True
                        visited.add(id)
                        q.append(id)
        return False

# s = "bb"
# dict = ["a", "b", "bbb", "bbbb"]
s = "leetcode"
dict = ['leet', 'code']
res = Solution().word_break_bfs(s, dict)
print(res)