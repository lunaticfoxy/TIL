/*
주소: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

내용
- 문자열과 단어의 배열이 주어진다
- 문자열을 하나씩 순회하며 단어의 배열을 이어붙여 문자열을 이어나갈 수 있는지 체크하고자 한다
  - 단어 배열이 빌때까지만 이으면 된다
- 이때 가능한 문자열 내에서의 인덱스를 모두 구하라

샘플
Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


풀이방법
- 단어를 맵으로 만들어 개수를 카운트한다
- 매 문자열 인덱스마다 단어중 매칭되는게 있는지 체크하고 해당 단어를 맵에서 하나씩 줄인뒤 반복한다

*/
object Solution {
  def findSubstring(s: String, words: Array[String]): List[Int] = {

    def checkString(s: String, wordMap: Map[String, Int]): Boolean = {
      //println(s + " / " + words.mkString(","))

      if(wordMap == null || wordMap.isEmpty)
        true
      else {
        val foundWord = wordMap.keys.filter(s.startsWith)

        if(foundWord == null || foundWord.isEmpty)
          false
        else {
          val newFoundVal = wordMap(foundWord.head) - 1
          val newWordMap = if(newFoundVal == 0) wordMap - foundWord.head
          else (wordMap - foundWord.head) + (foundWord.head -> newFoundVal)


          checkString(s.drop(foundWord.head.length), newWordMap)
        }
      }
    }


    def findSubStringRecur(s: String, newWordMap: Map[String, Int], idx: Int, indicies: List[Int]): List[Int] = {
      if(s == null || s.isEmpty)
        indicies
      else if(checkString(s, newWordMap))
        findSubStringRecur(s.drop(1), newWordMap, idx + 1, indicies ++ List(idx))
      else
        findSubStringRecur(s.drop(1), newWordMap, idx + 1, indicies)
    }

    val wordMap = words.groupBy(identity).map{case (k: String, v: Array[String]) => (k, v.length)}.toMap
    findSubStringRecur(s, wordMap, 0, List[Int]())

  }
}
