"""
주소: https://leetcode.com/problems/find-all-good-strings/

내용
- 같은 길이의 문자열 2개와 evil 문자열이 주어진다
  - 2번 문자열은 항상 1번 문자열보다 사전순으로 크다
- evil 문자열을 substring으로 포함하지 않는 문자열을 good string 이라 부른다
- 1번 문자열과 2번 문자열 사이에 있는 문자열 중 good string의 개수를 리턴하라
  - 1번 문자열, 2번 문자열도 포함한다
  
  
샘플
Example 1:
Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da". 

Example 2:
Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.

Example 3:
Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2

풀이방법
- 
"""
