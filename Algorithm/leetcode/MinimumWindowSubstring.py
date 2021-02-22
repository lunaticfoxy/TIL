"""
주소: https://leetcode.com/problems/minimum-window-substring/

내용
- 문자열 s, t가 주어진다
- 문자열 s내에서 t에 나온 문자들을 t에 나온 횟수만큼 포함하는 최소 길이의 substring을 찾아라

예제
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"


풀이방법
- 더블 포인터 사용
- 먼저 앞에서부터 체크하여 t의 원소를 모두 포함하는 l, r을 찾는다
- 이후 r을 현재 l과 같은 값이 나오는 지점까지 증가시킨다
- 그리고 l을 조건에 만족하는 지점까지 증가시키고 해당 시점의 길이가 최소 길이보다 작으면 갱신한다
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        
        l = 0
        r = 0
        cur_cnt = dict()
        t_remain = set(t)
        
        while r < len(s):
            if s[r] in t_counter:
                if s[r] in cur_cnt:
                    cur_cnt[s[r]] += 1
                else:
                    cur_cnt[s[r]] = 1
            
                if s[r] in t_remain and cur_cnt[s[r]] >= t_counter[s[r]]:
                    t_remain.remove(s[r])
                    
                    if len(t_remain) == 0:
                        break
        
            r += 1
            if len(cur_cnt) == 0:
                l += 1
        
        if len(t_remain) > 0:
            return ""
        
        #print(l, r)
        #print(s[l:r+1])
        #print(cur_cnt)
        while l < r:
            if s[l] in t_counter:
                if cur_cnt[s[l]] > t_counter[s[l]]:
                    cur_cnt[s[l]] -= 1
                else:
                    break
            l += 1
        
        min_r = r
        min_l = l
        min_len = r - l + 1
        
        #print(min_l, min_r)
        #print(s[min_l:min_r+1])
        #print(cur_cnt)
        r += 1
        while r < len(s):
            if s[r] in t_counter:
                cur_cnt[s[r]] += 1
            
                if s[r] == s[l]:
                    while True:
                        if s[l] in t_counter:
                            cur_cnt[s[l]] -= 1
                        
                        l += 1
                        if r - l + 1 < min_len:
                            min_len = r - l + 1
                            min_r = r
                            min_l = l
                        
                        #print(min_l, min_r)
                        #print(s[min_l:min_r+1])
                        #print(cur_cnt)
                        
                        if l>= r or (s[l] in t_counter and t_counter[s[l]] == cur_cnt[s[l]]):
                            break
            r += 1
        
        return s[min_l:min_r+1]
                
        
