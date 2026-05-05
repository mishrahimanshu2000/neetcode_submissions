class Twitter:

    def __init__(self):
        self.followings = defaultdict(set)
        self.posts = defaultdict(list)  
        self.postTime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.postTime, tweetId))
        self.postTime+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.followings[userId].add(userId)
        for following in self.followings[userId]:
            for posts in self.posts[following]:
                heapq.heappush(heap,posts)
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = []
        while heap:
            _,tweet = heapq.heappop(heap)
            res.append(tweet)
        
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)