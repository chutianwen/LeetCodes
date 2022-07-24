'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be
posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

'''
import itertools
import collections
import heapq

class Twitter2(object):

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key: userID, value: feeds in a queue
        self.user_feeds = dict()
        # key: userID, value: followeeID in a set
        self.user_following = dict()
        # Timeframe data, to make sure each post is unique
        self.time_frame = 0.0
        #

    def initialize(self, userID):
        self.user_following.setdefault(userID, set())
        self.user_following[userID].add(userID)
        self.user_feeds.setdefault(userID, [])

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.time_frame += 1
        self.initialize(userId)
        # update such userId's followers' feed pools
        for listener in self.user_following:
            # If such user follows this userID.
            if userId in self.user_following[listener]:
                self.user_feeds[listener].append((tweetId, userId, self.time_frame))
                # trim the size to avoid feeds explosion.
                # if len(self.user_feeds[listener]) > 10:
                #     self.user_feeds[listener] = self.user_feeds[listener][-10:]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId in self.user_feeds:
            feeds = self.user_feeds[userId][-1:-11:-1]
            return list(map(lambda x: x[0], feeds))
        else:
            return []

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.initialize(followerId)
        self.initialize(followeeId)
        # Only add followeeId if followerId has not followed followeeId, avoid append followeeId's feeds multiple times
        if followeeId not in self.user_following[followerId]:
            self.user_following[followerId].add(followeeId)
            if followerId != followeeId and self.user_feeds[followeeId]:
                # only add followeeId's feeds to followerId, prevent adding followeeId's feeds which were from followerId
                feeds_from_followeeId = list(filter(lambda x: x[1] == followeeId, self.user_feeds[followeeId]))
                self.user_feeds[followerId].extend(feeds_from_followeeId[-10:])
                self.user_feeds[followerId].sort(key=lambda x: x[2])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.initialize(followerId)
        self.initialize(followeeId)
        if followerId != followeeId and followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)
            # remove followerId's feed which were from followeeId
            self.user_feeds[followerId] = list(filter(lambda x: x[1] != followeeId, self.user_feeds[followerId]))


twitter = Twitter()

twitter.postTweet(1, 1)

print(twitter.getNewsFeed(1))

# User 2 follows user 1.
twitter.follow(2, 1)

print(twitter.getNewsFeed(2))

twitter.unfollow(2, 1)

print(twitter.getNewsFeed(2))
