"""
주소: https://leetcode.com/problems/count-sorted-vowel-strings/

내용
- a, e, i, o, u 문자만 사용해서 문자열을 만들려고 한다
- 이때 뒤에 나오는 문자는 앞의 문자보다 사전순으로 앞에 나와서는 안된다
  - oo (o), ae (o), ie (x), ua (x)
- 길이 n이 주어질 때 만들 수 있는 문자열을 수를 모두 구하라

예제
Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045


풀이방법
- dp를 사용한다
- a:5, e:4, i:3, o:2, u:1 로 치환하여 연산이 쉽게 한다
- dp[k][n] 에는 k문자보다 크거나 같은 문자로 만들 수 있는 n 길이의 문자열 개수를 저장한다
- 이때 다음과 같은 점화식이 성립한다
  - dp[1][n] = 1
  - dp[k][n] = 1 + dp[k-1][n] + dp[k-1][n-1] + ... + dp[k-1][1]
    - 1은 k로만 이루어진 문자열이다 (ex - aaaa)
    - dp[k-1][n]은 k보다 작은 문자로만 만든 길이 n의 문자열이다 (ex - eeee, eeiu)
    - dp[k-1][n-x]는 k보다 작은 문자로만 만든 길이 n-x의 문자열로 앞에 k 문자를 붙일것이다 (ex - aaee, aaae, aiuu)
- 따라서 dp[5][n] 까지 k, n을 증가시키면서 계산하여 저장하고 dp[5][n]을 리턴한다


"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = dict()
        dp[1] = dict()
        dp[2] = dict()
        dp[3] = dict()
        dp[4] = dict()
        dp[5] = dict()
        
        for k in range(1,6):
            for i in range(1, n+1):  
                dp[k][i] = 1
                if k>1:
                    for j in range(1,i+1):
                        dp[k][i] += dp[k-1][j]
        
        return dp[5][n]
