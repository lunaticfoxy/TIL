"""
주소: https://leetcode.com/problems/find-the-town-judge/


내용
- N명의 마을사람이 있는데 이중에 판사가 1명 있거나 없다
- 그리고 사람들의 신뢰 관계 (일방향) 이 주어진다.
- 판사는 자기 자신을 포함해서 아무도 믿지 않는다.
- 판사가 아닌 마을 사람들은 모두 판사를 믿는다
- 판사를 찾고 없으면 -1을 리턴하라 (인덱스는 1부터 시작)


샘플
Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


풀이방법
- 논리문제니 논리적으로 접근하자
- 먼저 후보 리스트에 모든 사람을 넣는다
- 이후 다음 과정을 모든 신뢰관계에 대해 반복한다
  - 한번이라도 누군가를 신뢰한 사람은 판사 후보에서 제외한다
  - 신뢰를 받은사람은 신뢰 횟수를 카운트한다
- 모든 신뢰관계 체크 이후 후보가 남아있다면 각 후보들의 신뢰 횟수를 확인해본다
- 신뢰 횟수가 N-1 (판사를 제외한 나머지 모두) 인 사람이 한명 있다면 그사람이 판사일것이다

"""
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        cands = set([i for i in range(N)])
        counts = [0 for _ in range(N)]
        
        for each in trust:
            if (each[0]-1) in cands:
                cands.remove(each[0]-1)
                
            counts[each[1]-1] += 1
        
        if len(cands)==0:
            return -1
        
        cands_list = []
        for cand in cands:
            if counts[cand] == N-1:
                cands_list.append(cand)
        
        if len(cands_list)==1:
            return cands_list[0]+1
        
        return -1
        
            
        
                
