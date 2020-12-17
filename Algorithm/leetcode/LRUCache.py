"""
주소: https://leetcode.com/problems/lru-cache/

내용
- LRU 캐시를 구현하라
- 캐시는 key-value 형태로 데이터를 저장한다
- 캐시는 초기화 단계에서 capacity를 가진다
- capacity가 넘어가면 가장 사용한지 오래된 데이터부터 삭제한다
- get, put 함수는 모두 O(1) 시간복잡도를 지닌다

예제
Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


풀이 방법
- 더블 링크드리스트를 사용해서 데이터의 사용 시점을 고려한다
- 가장 최근에 사용한 데이터를 tail, 가장 나중에 사용한 데이터를 head에 둔다
- 기존에 있던 key가 들어오면 해당 노드를 tail의 뒤로 옮긴다
  - 혹시 값이 바꼈으면 값도 갱신한다
- 기존에 없던 key가 들어왔으면 tail 뒤에 새로운 노드를 붙인다.
  - 이때 capacity 넘어갔으면 head를 지운다
  - 실제 구현은 객체를 최대한 재사용하려고 head를 tail뒤로 보냈다
- key에 해당하는 데이터가 있는지 여부는 map을 통해 체크한다
  - map은 key를 입력으로 해당 key에 해당하는 데이터가 저장된 노드의 주소를 저장한다.


"""
class ListNode(object):
    def __init__(self, key, val, before_node, next_node):
        self.key = key
        self.val = val
        self.before = before_node
        self.next = next_node

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.node_map = dict()
        self.cnt = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        """
        print("------get------")
        print(key)
        print(self.node_map.keys())
        printList(self.head)
        printListReverse(self.tail)
        """
        
        if key in self.node_map:
            temp = self.node_map[key]
            
            if not temp == self.tail:
                self.tail.next = temp
                
                if self.head == temp:
                    self.head = temp.next
                else:
                    temp.before.next = temp.next
                
                temp.next.before = temp.before
                temp.before = self.tail
                temp.next = None
                self.tail = temp
                
            return temp.val
        else:
            return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.node_map:
            temp = self.node_map[key]
            
            if not temp == self.tail:
                self.tail.next = temp
                
                if self.head == temp:
                    self.head = temp.next
                else:
                    temp.before.next = temp.next
                
                temp.next.before = temp.before
                temp.before = self.tail
                temp.next = None
                self.tail = temp
            
            temp.val = value
        else:
            if self.cnt == self.capacity:
                del self.node_map[self.head.key]
                
                if self.capacity > 1:
                    temp = self.head
                    self.head = temp.next
                    self.head.before = None
                    self.tail.next = temp
                    temp.before = self.tail
                    temp.next = None
                    self.tail = temp
                    
                self.tail.key = key
                self.tail.val = value
            elif self.head == None:
                self.tail = ListNode(key, value, None, None)
                self.head = self.tail
                self.cnt += 1
            else:
                self.tail.next = ListNode(key, value, self.tail, None)
                self.tail = self.tail.next
                self.cnt += 1
            self.node_map[key] = self.tail
        
        """
        print("------put------")
        print(self.node_map.keys())
        printList(self.head)
        printListReverse(self.tail)
        """
        


def printList(head):
    strs = ""
    if head==None:
        print(None)
    
    cur = head
    
    while cur:
        strs += str(cur.key)
        strs += " "
        cur = cur.next
    
    print(strs)
    
def printListReverse(tail):
    strs = ""
    if tail==None:
        print(None)
    
    cur = tail
    
    while cur:
        strs += str(cur.key)
        strs += " "
        cur = cur.before
    
    print(strs)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
