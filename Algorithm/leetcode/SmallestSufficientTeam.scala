"""
주소: https://leetcode.com/problems/smallest-sufficient-team/

내용
- 신규 팀원을 뽑으려고 한다
- 팀에서 필요한 스킬셋과 각 사람의 스킬셋이 주어진다
- 필요한 스킬셋을 만족시킬 수 있는 최소한의 멤버를 계산하라

샘플
Example 1:
Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]

Example 2:
Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]

풀이방법
- 재귀로 시도
  - 먼저 필요한 스킬셋과 사람별 스킬셋을 set으로 만듬
  - 이후 한명씩 비교하면서 넣었을때와 아닐때를 재귀로 나누어 탐색
    - 이때 남은 스킬셋을 충족하는 경우만 넣음
  - 스킬셋이 모두 충족되면 현재까지 인원 리턴
  - 스킬셋이 충족되지 않았는데 남은 인원이 없으면 null 리턴
  - 답은 나오나 타임리밋 발생
- 재귀 시도 2차
  - 다음 시도는 스킬셋 단위로 스킬을 가지고 있는 사람의 인덱스를 저장하도록 구성
  - 이후 스킬셋 단위로 재귀를 돌면서 해당 스킬을 가지고 있는 사람을 한명씩 선택하면서 다음 단계로 재귀 수행
    - 이때 선택된 사람이 포함된 스킬은 지우고 탐색
"""
object Solution {
    def smallestSufficientTeam(req_skills: Array[String], people: List[List[String]]): Array[Int] = {
        
        def recurFunc(reqSkill: Array[Set[Int]], people: Array[Int]): Array[Int] = {
            if(reqSkill.size == 0)
                people
            else if(reqSkill(0).size == 0)
                null
            else {
                val temp = reqSkill(0).map{person => 
                    recurFunc(reqSkill.drop(1).filter(x => !x.contains(person)), people ++ Array(person))
                }.filter(x => x != null)
                
                temp.reduce((x, y) => if(x.size < y.size) x else y)
            }
        }
        
        val peopleWithIdx = people.zipWithIndex
        
        val reqSkill = req_skills.map{x =>
            peopleWithIdx.filter(y => y._1.contains(x)).map(_._2).toSet
        }.toArray
        
        recurFunc(reqSkill, Array[Int]())
    }
}
