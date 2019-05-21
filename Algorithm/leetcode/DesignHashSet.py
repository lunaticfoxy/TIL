"""
주소: https://leetcode.com/problems/design-hashset/

내용
- add, remove, contains를 메소드로 가지고있는 MyHashSet을 구현하라

샘플
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)


풀이방법
- 풀이 자체보다는 내장 자료구조는 리스트만 활용해서 풀어보는걸 목적으로 하자
- 2단계 해싱 사용
  - 1단계: value의 100단위 이하 100 자리
  - 2단계: value의 100단위부터 10000단위 까지 100자리
- 3중 리스트를 만들어 1단계 해싱, 2단계 해싱, 값 기준으로 저장
- 이후는 단순 탐색하면서 풀이 수행


"""
class MyHashSet:

    def hashing(self, value):
        lv1 = value%100
        lv2 = (value//100)%100
        return lv1, lv2
        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cont = [[[] for _ in range(101)] for _ in range(101)]
        
        

    def add(self, key: int) -> None:
        lv1, lv2 = self.hashing(key)
        
        for item in self.cont[lv1][lv2]:
            if item==key:
                return
        
        self.cont[lv1][lv2].append(key)
        

    def remove(self, key: int) -> None:
        lv1, lv2 = self.hashing(key)
        
        for i, item in enumerate(self.cont[lv1][lv2]):
            if item==key:
                del self.cont[lv1][lv2][i]
                return
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        lv1, lv2 = self.hashing(key)
        
        for item in self.cont[lv1][lv2]:
            if item==key:
                return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
