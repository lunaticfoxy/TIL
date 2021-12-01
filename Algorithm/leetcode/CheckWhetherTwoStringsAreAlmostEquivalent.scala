/*
주소: https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

내용
- 단어 두개가 두어진다
- 두 단어를 구성하는 글자중 개수의 차이가 4이상인 글자가 없으면 almost equivalent 라 한다
- 두 단어가 almost equivalent 인지 여부를 리턴하라


예제
Example 1:
Input: word1 = "aaaa", word2 = "bccb"
Output: false
Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
The difference is 4, which is more than the allowed 3.

Example 2:
Input: word1 = "abcdeef", word2 = "abaaacc"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
- 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
- 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
- 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
- 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
- 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.

Example 3:
Input: word1 = "cccddabba", word2 = "babababab"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
- 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
- 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
- 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.


풀이방법
- 단순 카운트 후 비교
*/

object Solution {
  def checkAlmostEquivalent(word1: String, word2: String): Boolean = {
    val word1Map = word1.toArray.groupBy(x => x).map{x =>
      (x._1, x._2.size)
    }.toMap

    val word2Map = word2.toArray.groupBy(x => x).map{x =>
      (x._1, x._2.size)
    }.toMap

    val keys = word1Map.keys.toSet ++ word2Map.keys.toSet

    keys.filter{k =>
      val word1Cnt = if(word1Map.contains(k)) word1Map(k) else 0
      val word2Cnt = if(word2Map.contains(k)) word2Map(k) else 0

      Math.abs(word1Cnt - word2Cnt) > 3
    }.isEmpty
  }
}
