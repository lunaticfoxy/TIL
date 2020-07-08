"""
주소: https://leetcode.com/problems/flipping-an-image/

내용
- 1, 0으로 이루어진 이미지를 좌우로 뒤집고 1/0을 반전시키자

샘플
Example 1:
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:
Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

풀이방법
- 단순 구현

"""
object Solution {
    def flipAndInvertImage(A: Array[Array[Int]]): Array[Array[Int]] = {
        
        def recurFunc(A: Array[Array[Int]], res: Array[Array[Int]]): Array[Array[Int]] = {
            if(A.size == 0)
                res
            else
                recurFunc(A.drop(1), res ++ Array(A(0).reverse.map(x => (x + 1) % 2)))
        }
        
        recurFunc(A, Array[Array[Int]]())
    }
}
