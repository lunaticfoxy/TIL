/*
주소: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

내용
- 문자열의 배열이 주어진다
- 문자열 내의 단어 수가 가장 많은 문자열의 단어 수를 리턴하라

예제
Example 1:
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

Example 2:
Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
Explanation: It is possible that multiple sentences contain the same number of words. 
In this example, the second and third sentences (underlined) have the same number of words.

풀이방법
- 단순구현
*/

object Solution {
    def mostWordsFound(sentences: Array[String]): Int = {
        sentences.map{s =>
            s.split(" ").size
        }.max
    }
}
