'''
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it
returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm
should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the
original URL.
'''

import collections
import string
import random
class CodecB_Random:
    '''
    It is also good to combine the timeframe into the shortened data
    '''
    def __init__(self):
        self.url_pool = collections.defaultdict(str)
        self.chr_pool = string.ascii_letters + string.digits
        self.length_shorter_url = 6
        self.prefix = 'http://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        'http://tinyurl.com/'
        :type longUrl: str
        :rtype: str
        """
        shorterURL = ''
        while shorterURL in self.url_pool:
            shorterURL = ''
            for i in range(self.length_shorter_url):
                shorterURL += self.chr_pool[random.randint(0, self.length_shorter_url-1)]
        self.url_pool[shorterURL] = longUrl
        return self.prefix + shorterURL

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[len(self.prefix):]
        return self.url_pool.get(key)

class Codec:

    def __init__(self):
        self.url_pool = collections.defaultdict(str)
        self.prefix = 'http://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        'http://tinyurl.com/'
        :type longUrl: str
        :rtype: str
        """
        hash_code = hash(longUrl)
        self.url_pool[hash_code] = longUrl
        return self.prefix + str(hash_code)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        key = int(shortUrl[len(self.prefix):])
        return self.url_pool.get(key)


# Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
res = codec.decode(codec.encode(url))
print(res)
