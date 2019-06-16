"""
주소: https://leetcode.com/problems/letter-tile-possibilities/

내용
- 영어 대문자로 이루어진 문자열이 주어진다
- 이 문자열에 포함된 문자를 사용해서 만들 수 있는 모든 문자열의 개수를 구하라
  - 결과 중복 미허용
  - 순서 변경 가능
  - 미사용 가능
  - 공백 문자열 제외

샘플
Example 1:
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: "AAABBC"
Output: 188

풀이방법
- 딱히 없다
- 그냥 모든 경우의수를 구한다
  - 혹시 몰라서 디스커스를 봤는데 맞는듯...
  - 그냥 현재 로직에 프루닝 더할 수 있음
- 조합을 구해야 하므로 문자의 수를 카운트한다
- 이후 재귀 함수 findRes를 돈다
  - 재귀가 일어나면서 현재 남은 문자를 넘어온 문자열에 이어붙인다
  - 이어 붙인 문자열이 기존에 없던 문자면 추가한다
  - 남은 문자에서 이어붙인 문자를 빼고 다시 재귀를 돌린다
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        resSet = set()
        charDict = dict()
        
        for tile in tiles:
            if tile in charDict:
                charDict[tile] += 1
            else:
                charDict[tile] = 1
        
        def findRes(last, leftTiles):
            for tile in leftTiles:
                if leftTiles[tile]==0:
                    continue
                    
                temp = last + tile
                if not temp in resSet:
                    resSet.add(temp)
                    
                newLeftTiles = dict(leftTiles)
                newLeftTiles[tile] -= 1
                
                findRes(temp, newLeftTiles)
        
        findRes("", charDict)
        
        return len(resSet)
