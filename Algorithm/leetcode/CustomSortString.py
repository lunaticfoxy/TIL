"""
주소: https://leetcode.com/problems/custom-sort-string/

내용
- 정렬 순서를 담은 문자열 S가 주어진다
  - S에는 영어 소문자만 들어있다.
  - S에 나타난 문자는 해당 순서대로 정렬된다
  - S에 나타나지 않은 문자는 S에 나타난 문자 이후에 사전순으로 정렬된다
- 새로 주어진 문자열 T를 S의 정렬 규칙에 맞춰 정렬하라


샘플
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

풀이방법
- 헷갈리지 않게 문자를 숫자로 변환한뒤 정렬하고 다시 변환한다
- 이를 위해서 S[0]=0, S[1]=1, ..., S[n]=n 으로 변환할수 있게 sDict를 만들고 S에 나타나지 않은 문자는 이후에 이어붙인다
- 반대 방향으로 0->S[0], 1->S[1], ... 로 변환 가능한 sList를 만든다
- 이후에는 T를 sDict를 이용해 변환한 뒤 정렬하고 다시 sList를 통해 역변환해서 문자열로 합친다

"""

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        sList = [char for char in S]
        sDict = dict()
        
        for i in range(len(sList)):
            sDict[sList[i]] = i
        
        aOrd = ord("a")
        for i in range(26):
            c = chr(aOrd + i)
            
            if c in sDict:
                continue
                
            sDict[c] = len(sList)
            sList.append(c)
        
        tConv = sorted([sDict[char] for char in T])
        newT = "".join([sList[idx] for idx in tConv])
        return newT
        
