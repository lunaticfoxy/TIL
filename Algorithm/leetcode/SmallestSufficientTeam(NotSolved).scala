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
"""
object Solution {
    def smallestSufficientTeam(req_skills: Array[String], people: List[List[String]]): Array[Int] = {
        
        
        def recurFunc(reqSkill: Set[String], people: List[Set[String]], idx: Int, idxs: Array[Int]): Array[Int] = {
            if(reqSkill.size == 0)
                idxs
            else if(people.size == 0)
                null
            else {
                val cont = if(reqSkill.intersect(people(0)).size == 0) null else recurFunc(reqSkill.filter(x => !people(0).contains(x)), people.drop(1), idx + 1, idxs ++ Array(idx))
                val notCont = recurFunc(reqSkill, people.drop(1), idx + 1, idxs)
                
                if(cont == null)
                    notCont
                else if(notCont == null)
                    cont
                else {
                    if (cont.size > notCont.size)
                        notCont
                    else
                        cont
                }
            }
        }
        
        
        recurFunc(req_skills.toSet, people.map(_.toSet), 0, Array())
    }
}
