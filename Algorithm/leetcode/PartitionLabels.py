"""
주소: https://leetcode.com/problems/partition-labels/


내용
- 문자열이 주어지는데 이 문자열에는 여러 문자가 섞여있다.
- 같은 문자는 한 파티션에만 속하도록 파티션을 나누려 한다.
- 나눌수 있는 최대한 파티션을 나누고, 그 파티션들의 길이를 리스트로 반환하라


샘플
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


풀이방법
- 한 문자는 다 한 파티션 안에 들어가야되니 문자별로 시작 지점이랑 끝지점을 찾아야 함
- 그리고 구간이 겹치는 문자끼리는 한 파티션에 넣어야 함
  - 사실상 스케줄링할때 겹치는거 합치는 문제와 동일
- 이걸 빠르겨 하려면 일단 구간을 시작 값 기준으로 정렬하고
- 새로운 구간을 하나씩 보면서 앞이랑 겹치는 구간이면 둘을 합침
  - 실제 구현시에는 앞의 구간의 끝을 갱신하는 식으로 진행
- 머지가 끝난 뒤 각 구간의 길이를 리턴하면 됨
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        charLoc = dict()
        for i in range(len(S)):
            if not S[i] in charLoc:
                charLoc[S[i]] = [i]
            else:
                charLoc[S[i]].append(i)
        
        tempParts = []
        for c in charLoc:
            tempParts.append([charLoc[c][0], charLoc[c][-1]])
        
        tempParts = sorted(tempParts, key=lambda x:x[0])
        parts = []
        res = []
        for part in tempParts:
            if len(parts)==0:
                parts.append(part)
            elif parts[-1][1]<part[0]:
                res.append(parts[-1][1] - parts[-1][0] + 1)
                parts.append(part)
            else:
                parts[-1][1] = max(parts[-1][1], part[1])
        
        res.append(parts[-1][1]-parts[-1][0]+1)
        return res
        
                
