"""
주소: https://leetcode.com/problems/design-twitter/

내용
- 트위터 로직을 재현해보자
- 트위터의 다음 기능을 구현하라
  - 트윗 포스트: 새로운 트윗을 올림
  - 뉴스피드 가져오기: 자기 자신과 자기가 팔로우하는 사람의 최근 트윗 10개를 가져오기
  - 팔로우: 소식을 받아볼 사람 등록
  - 언팔로우: 소식을 받아볼 사람 삭제

예제
Example 1:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


풀이방법
- 단순 구현
- 포스트는 리스트, 팔로워는 set의 map으로 관리
"""
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.posts = []
        self.follows = dict()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts.append([userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        cnt = 0
        idx = 0
        res = []
        
        while cnt < 10 and idx < len(self.posts):
            cur_post = self.posts[-(idx + 1)]
            if cur_post[0] == userId or (userId in self.follows and cur_post[0] in self.follows[userId]):
                res.append(cur_post[1])
                cnt += 1
            idx += 1
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set([followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
