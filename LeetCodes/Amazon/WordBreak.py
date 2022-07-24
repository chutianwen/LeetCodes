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

        from collections import defaultdict
        explored = defaultdict
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


    def wordBreakDP(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(len(s) - 1, i-1, -1):
                if dp[i] and s[i: j+1] in wordDict:
                    if j == len(s) - 1:
                        return True
                    dp[j+1] = True

        return False

    def wordBreakDP2(self, s, wordDict):

        words = set(wordDict)
        cache = [False] * (len(s) + 1)
        cache[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if cache[j] and s[j: i] in words:
                    cache[i] = True
                    break
        return cache[-1]

class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or len(s):
            return False

        word_dict_trim = set(filter(lambda word: word in s, wordDict))
        print(word_dict_trim)
        frontier = [""]
        explored = set()
        while frontier:
            expand = frontier.pop()
            print(expand)
            for word in wordDict:
                future = expand + word
                if future == s:
                    return True
                elif len(future) < len(s) and s.startswith(future) and future not in explored:
                    frontier.append(future)
                    explored.add(future)
        return False


class TrieNode(object):
    def __init__(self, char=None, isWord=False):
        self.char = char
        self.isWord = isWord
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.cache = {}

    def insert(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.isWord = True

    def cache(f):
        def method(obj, s):
            if s not in obj.cache:
                obj.cache[s] = f(obj, s)
            return obj.cache[s]
        return method

    @cache
    def search(self, s):
        root = self.root
        for i, char in enumerate(s):
            if char not in root.children:
                return False

            if root.children[char].isWord:
                if self.search(s[i + 1:]):
                    return True     

            root = root.children[char]
        return root.isWord


class Solution3(object):
    def wordBreak(self, s, wordDict):
        trie = Trie()
        [trie.insert(word) for word in wordDict]

        return trie.search(s)

class Solution4:
    def wordBreak(self, s, wordDict):
        """
        Optimal
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        explored = dict()
        stop = len(s)
        words = set(wordDict)

        def dfs(start):
            if start == stop:
                return True

            for split in range(start + 1, stop + 1):
                if split in explored:
                    continue

                part_left = s[start: split]
                if part_left in words and dfs(split):
                    return True

            explored[start] = False
            return False

        return dfs(0)


# s = "bb"
# dict = ["a", "b", "bbb", "bbbb"]
s = ""
dict = ['leet', 'code', ""]
res = Solution3().wordBreak(s, dict)
print(res)


from collections import defaultdict
def cache(f):
    cache = defaultdict(int)

    def method(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return method

@cache
def fun(x):
    sum = 0
    for v in range(x):
        sum += v
    return sum
