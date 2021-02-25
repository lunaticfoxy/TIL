/*
주소: https://leetcode.com/problems/simplify-path/

내용
- 패스가 문자열로 주어진다
- 이 패스중 생략할 수 있는 부분을 모두 없애라
  - /./ => /
  - /temp/../ => /temp
  - temp/ => temp
  - a//b => a/b

예제
Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: path = "/a/./b/../../c/"
Output: "/c"


풀이방법
- 단순 구현
- 꼬리재귀로 돌면서 / 단위로 잘라 처리
*/
object Solution {
  def simplifyPath(path: String): String = {

    def recurSimplifyPath(curPath: String, remainedPath: String): String = {
      if(remainedPath.isEmpty)
        return if(curPath.isEmpty) "/" else curPath

      val front = remainedPath.indexOf("/")
      val subStr = if(front < 0) remainedPath else remainedPath.substring(0, front)
      //println("---------------")
      //println(curPath)
      //println(remainedPath)
      //println(subStr)

      val newRemainedPath = remainedPath.drop(subStr.length + 1)

      val newCurPath =
        if(subStr.length == 0 || subStr == ".") curPath
        else if(subStr == "..") {
          val curLast = curPath.lastIndexOf("/")

          if(curLast < 0)
            ""
          else
            curPath.substring(0, curLast)
      } else
        curPath + "/" + subStr

      recurSimplifyPath(newCurPath, newRemainedPath)
    }

    recurSimplifyPath("", path)
  }
}
