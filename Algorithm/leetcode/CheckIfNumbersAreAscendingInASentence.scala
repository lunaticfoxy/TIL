/*
주소: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

내용
- 문자와 [0, 100] 구간 사이의 숫자로 이루어진 문장이 주어진다
- 숫자와 문자는 모두 스페이스로 구분되어있다
- 이때 문장 내에 나타나는 숫자가 증가하는지 여부를 리턴하라

예제
Example 1:
example-1
Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
Output: true
Explanation: The numbers in s are: 1, 3, 4, 6, 12.
They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.

Example 2:
Input: s = "hello world 5 x 5"
Output: false
Explanation: The numbers in s are: 5, 5. They are not strictly increasing.

Example 3:
example-3
Input: s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
Output: false
Explanation: The numbers in s are: 7, 51, 50, 60. They are not strictly increasing.

Example 4:
Input: s = "4 5 11 26"
Output: true
Explanation: The numbers in s are: 4, 5, 11, 26.
They are strictly increasing from left to right: 4 < 5 < 11 < 26.


풀이
- 단순구현
*/


object Solution {
    def areNumbersAscending(s: String): Boolean = {
        
        def isIncreasing(arr: Array[Int]): Boolean = {
            if(arr.size <= 1)
                true
            else if(arr(0) >= arr(1))
                false
            else
                isIncreasing(arr.drop(1))
        }
        
        val numberChar = Set('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        
        isIncreasing(s.split(" ").filter(x => numberChar.contains(x(0))).map(_.toInt))
    }
}
