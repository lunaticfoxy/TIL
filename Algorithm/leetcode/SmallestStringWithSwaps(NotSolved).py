"""
주소: https://leetcode.com/problems/smallest-string-with-swaps/

내용
- 문자열과 문자열 내 인덱스의 쌍이 0개 이상 주어진다
- 인덱스의 쌍에 해당하는 문자는 서로 위치를 교환할 수 있다
- 교환 횟수에 제한이 없을때 교환을 통해 만들수있는 사전순서에서 가장 빠른 문자열을 구하라

예제
Example 1:
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"


풀이과정
- 일단 이거 통과 못한 문제
  - 로직은 맞는듯하나 타임리밋 발생
- 푼 로직 설명
  - 교환을 무한정 할 수 있으므로 교환 가능한 모든 쌍끼리는 사실 연결된다
    - [0,1], [1,3] 이 있다면 [0,1,3]은 사실 하나의 집합
  - 따라서 먼저 모든 연결되는 집합의 탐색이 필요
  - 이후 연결 집합에 들어가지 않는 인덱스는 하나의 집합으로 만듬
  - 모든 집합을 순회하며 해당 집합에 들어가는 문자들을 사전순으로 정렬하고
  - 이후 인덱스를 기준으로 다시 정렬하여 문자열 생성
- "모든 연결되는 집합의 탐색" 이부분이 지금 매번 반복되도록 짜여져 있음
  - 이부분에서 속도 향상이 필요할 것으로 보인다
  - 그래프 집합 탐색 방식으로 가능해보이긴 함

"""
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        pairSets = [set(pair) for pair in pairs]
        
        loop = True
        while loop:
            loop = False
            
            for i in range(len(pairSets)-1):
                tmp1 = pairSets[i]
                for j in range(i+1, len(pairSets)):
                    tmp2 = pairSets[j]
                    if len(tmp1 & tmp2)>0:
                        loop = True
                        pairSets.append(tmp1 | tmp2)
                        pairSets.remove(tmp2)
                        pairSets.remove(tmp1)
                        break
                
                if loop:
                    break
        
        for i in range(len(s)):
            notIn = True
            for ps in pairSets:
                if i in ps:
                    notIn = False
                    break
            
            if notIn:
                pairSets.append(set([i]))
        
        strList = []
        
        def getKey(item):
            return item[1]
        
        for ps in pairSets:
            strList.extend(zip(sorted([s[i] for i in ps]), sorted(ps)))
        
        return "".join(list(zip(*sorted(strList, key=getKey)))[0])
                    
        
