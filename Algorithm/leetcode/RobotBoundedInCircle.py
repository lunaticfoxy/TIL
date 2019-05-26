"""
주소: https://leetcode.com/problems/robot-bounded-in-circle/

내용
- 무한한 맵에 로봇의 명령어가 주어진다
  - G: 1칸 직진
  - L: 좌로 90도 방향 전환
  - R: 우로 90도 방향 전환
- 이 로봇의 경로가 원을 그리는지 여부를 리턴하라
  - 원을 그린다 = 로봇이 언젠가 시작 지점으로 돌아온다
  
  
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
- 코드 길어질 필요 없을텐데 생각하기 귀찮아서 깁니당...
- 두가지 요소 고려 필요
  - 좌표 체크
    - 어떻게 이동했건 최종 좌표가 (0, 0)으로 돌아 오는 경우는 무조건 True
    - 직접 시뮬레이션 하면서 좌표를 체크해서 확인
  - 좌표체크를 통과 하지 못했을 경우
    - 최종 방향이 변하면 무조건 True
      - 뱡향이 변하기만 하면 언젠가 돌아옴
    - 방향 체크는 l, r의 나타나는 횟수로
      - 두 값 횟수의 차이가 같으면 방향이 안변하니 False
      - 차이가 다르더라도 차이가 4의 배수면 한바퀴 돌아서 방향이 안변하니 False
      - 나머지 경우 전부 True

"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        gc = 0
        lc = 0
        rc = 0
        x = 0
        y = 0
        drt = 0
        for char in instructions:
            if char=='G':
                gc += 1
                if drt==0:
                    x += 1
                elif drt==1:
                    y += 1
                elif drt==2:
                    x -= 1
                else:
                    y -= 1
            elif char=="L":
                lc += 1
                if drt==0:
                    drt = 3
                elif drt==1:
                    drt = 0
                elif drt==2:
                    drt = 1
                else:
                    drt = 2
            else:
                rc += 1
                if drt==0:
                    drt = 1
                elif drt==1:
                    drt = 2
                elif drt==2:
                    drt = 3
                else:
                    drt = 0
                
        if x==0 and y==0:
            return True
        
        if lc==rc:
            return False
        
        diff = abs(lc-rc)
        
        if diff%4==0:
            return False
        
        return True
