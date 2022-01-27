/*
주소: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

내용
- 문자열의 배열이 주어진다
- 문자열 내에서 맨 처음으로 나타나는 Palindrome을 찾아서 리턴하라
  - 없다면 "" 를 리턴하라

예제
Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
  
풀이방법
- 단순구현
*/
object Solution {
    def firstPalindrome(words: Array[String]): String = {
        
        def isPalindrome(word: String): Boolean = {
            if(word.length <= 1)
                true
            else if(word.head == word.last)
                isPalindrome(word.substring(1, word.length - 1))
            else
                false
        }
        
        def recurFunc(words: Array[String]): String = {
            if(words.isEmpty)
                ""
            else {
                if(isPalindrome(words(0)))
                    words(0)
                else
                    recurFunc(words.drop(1))
            }
        }
        
        recurFunc(words)
    }
}
