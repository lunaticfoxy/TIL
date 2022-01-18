/*
주소: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

내용
- 문자열과 자연수 k, 문자 fill 이 주어진다
- 문자열을 k 길이 단위로 자르고, 마지막에 k보다 짧은 문자열이 생기면 fill 문자로 채워서 길이 k를 맞춰라


예제
Example 1:
Input: s = "abcdefghi", k = 3, fill = "x"
Output: ["abc","def","ghi"]
Explanation:
The first 3 characters "abc" form the first group.
The next 3 characters "def" form the second group.
The last 3 characters "ghi" form the third group.
Since all groups can be completely filled by characters from the string, we do not need to use fill.
Thus, the groups formed are "abc", "def", and "ghi".

Example 2:
Input: s = "abcdefghij", k = 3, fill = "x"
Output: ["abc","def","ghi","jxx"]
Explanation:
Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".


풀이방법
- 단순구현
*/
object Solution {
    def divideString(s: String, k: Int, fill: Char): Array[String] = {
        
        def recurFunc(s: String, k: Int, fill: String, curRes: Array[String]): Array[String] = {
            if(s.length == 0)
                curRes
            else if(s.length <= k)
                curRes ++ Array((s + (fill * (k - s.length))))
            else
                recurFunc(s.substring(k), k, fill, curRes ++ Array(s.substring(0, k)))
        }
                                
        recurFunc(s, k, fill.toString(), Array[String]())
    }
}
