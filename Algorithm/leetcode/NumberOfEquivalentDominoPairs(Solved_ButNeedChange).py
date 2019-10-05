"""
주소: https://leetcode.com/problems/number-of-equivalent-domino-pairs/

내용
- 숫자 쌍이 들어있는 리스트가 주어진다
- 이 쌍들 내에서 순서 무관하게 내부 원소가 동일한 pair를 찾고싶다
- 이때 존재하는 pair의 수를 리턴하라

예시
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

풀이방법
- 앞에서부터 모든 쌍을 구하면 타임리밋에 걸린다
- 어차피 한 쌍을 구하면 나머지 같은 종류도 한번에 계산 가능하다
  - [1,2], [2,1], [1,2] 가 있으면 두번에 나누지 않고 한번에 연산가능
- 따라서 그렇게 구했다
- 이때 동일노드 반복을 하지 않기 위해 founds에 이미 방문한 노드는 방문하지 않도록 한다
- 근데 아마 속도가 너무 느린듯한다
  - dp로 개선 가능?
  - 현재 O(n)이긴 한데 어디서 문제일까?

"""
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        founds = set()
        pairs = 0
        
        for i in range(len(dominoes) - 1):
            if i in founds:
                continue
            
            setCount = 0
            for j in range(i + 1, len(dominoes)):
                if j in founds:
                    continue

                if (dominoes[i][0]==dominoes[j][0] and dominoes[i][1]==dominoes[j][1]) or (dominoes[i][1]==dominoes[j][0] and dominoes[i][0]==dominoes[j][1]):
                    setCount += 1
                    
                    if not i in founds:
                        founds.add(i)
                    
                    founds.add(j)
            
            for i in range(setCount):
                pairs += (i+1)
            
        return pairs
