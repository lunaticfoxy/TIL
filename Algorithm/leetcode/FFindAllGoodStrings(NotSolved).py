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
- 재귀로 풀어보았으나 처음에는 메모리 리밋, 지금은 타임리밋 상태
- 메모리 리밋 시도
  - findGoodStrings를 재귀
  - 현재 string에 evil이 있으면 그대로, 아니면 + 1을 해서 재귀
  - 재귀시에 findNextString 함수로 다음 string을 s1 위치에 넣어줌
  - s1==s2이면 종료하되 evil이면 0, 아니면 1 리턴
- 타임 리밋 시도
  - findGoodStringsRecur을 재귀
  - 꼬리 재귀를 사용하기 위해 retVal을 인자로 넣어줌
  - s1==s2이면 종료하면서 retVal or retVal+1 리턴
  - 일단 에러가 바뀐거로 봐선 꼬리재귀로 들어가긴 한듯


"""
object Solution {
    def findGoodStrings(n: Int, s1: String, s2: String, evil: String): Int = {
        
        def findGoodStringsRecur(s1: String, s2: String, evil: String, retVal: Int): Int = {
        
            def findNextString(s: String): String = {
                val sArr = s.toArray

                def checkLast(arr:Array[Char]) : Array[Char] = {
                    //println(arr.mkString(","))
                    if(arr.size == 0)
                        arr
                    else {
                        if(arr.last == 'z')
                            checkLast(arr.dropRight(1)) :+ 'a'
                        else
                            arr.dropRight(1) :+ (arr.last.toInt + 1).toChar
                    }
                }

                checkLast(sArr).mkString("")
            }

            if(s1 == s2) {
                if(s1.contains(evil))
                    retVal
                else
                    retVal + 1
            }
            else {
                if(s1.contains(evil))
                    findGoodStringsRecur(findNextString(s1), s2, evil, retVal)
                else
                    findGoodStringsRecur(findNextString(s1), s2, evil, retVal + 1)
            }
        }
        
        findGoodStringsRecur(s1, s2, evil, 0)
    }
}
