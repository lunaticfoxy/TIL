"""
주소: https://leetcode.com/problems/robot-bounded-in-circle/

내용
- 로봇이 무한한 좌표 평면상에서 명령어에 따라 움직인다
  - G: 현재 방향으로 1칸 전진
  - L: 좌로 회전
  - R: 우로 회전
- 로봇의 경로가 루프인지 아닌지를 체크하라

샘플
Example 1:
Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:
Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.

Example 3:
Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

풀이방법
- 명령어가 한번 끝났을때 로봇의 방향이 처음과 같지 않다면 2턴 혹은 4턴 뒤에 돌아오게 되어있다
- 따라서 마지막 방향만 처음과 같은지 체크해주면 된다
- 단 마지막 방향이 처음과 같더라도 (0,0)이라면 이미 돌아왔으니 괜찮다

"""
object Solution {
    def isRobotBounded(instructions: String): Boolean = {
        
        def getLoc(inst: Array[Char], dir: Int, loc: (Int, Int)): ((Int, Int), Int) = {
            if(inst.size == 0)
                (loc, dir)
            else {
                val newDir = inst(0) match {
                    case 'G' => dir
                    case 'L' => if(dir == 0) 3 else dir - 1
                    case 'R' => (dir + 1) % 4
                }
                
                val newLoc = if(inst(0) == 'G') {
                    dir match {
                        case 0 => (loc._1 + 1, loc._2)
                        case 1 => (loc._1, loc._2 + 1)
                        case 2 => (loc._1 - 1, loc._2)
                        case 3 => (loc._1, loc._2 - 1)
                    }
                }
                else loc
                
                getLoc(inst.drop(1), newDir, newLoc)
            }
        }
        
        val (newLoc, newDir) = getLoc(instructions.toArray, 0, (0, 0))
        
        if(newDir != 0 || newLoc == (0, 0))
            true
        else
            false
    }
}
