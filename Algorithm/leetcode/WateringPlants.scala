/*
주소: https://leetcode.com/problems/watering-plants/

내용
- 화분의 개수만큼 배열이 주어진다
- 배열에는 화분에 줘야하는 물의 양이 있으며, 물은 -1 지점에서 떠온다고 한다
- 화분에 물을 준뒤 다음 화분에 물을 가득 줄 수 없으면 -1 지점으로 돌아와서 다시 물을 채우고 간다
- 모든 화분에 물을 주기 위해 몇걸음을 걸어야 하는지 계산하라


예제
Example 1:
Input: plants = [2,2,3,3], capacity = 5
Output: 14
Explanation: Start at the river with a full watering can:
- Walk to plant 0 (1 step) and water it. Watering can has 3 units of water.
- Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water.
- Since you cannot completely water plant 2, walk back to the river to refill (2 steps).
- Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water.
- Since you cannot completely water plant 3, walk back to the river to refill (3 steps).
- Walk to plant 3 (4 steps) and water it.
Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.

Example 2:
Input: plants = [1,1,1,4,2,3], capacity = 4
Output: 30
Explanation: Start at the river with a full watering can:
- Water plants 0, 1, and 2 (3 steps). Return to river (3 steps).
- Water plant 3 (4 steps). Return to river (4 steps).
- Water plant 4 (5 steps). Return to river (5 steps).
- Water plant 5 (6 steps).
Steps needed = 3 + 3 + 4 + 4 + 5 + 5 + 6 = 30.

Example 3:
Input: plants = [7,7,7,7,7,7,7], capacity = 8
Output: 49
Explanation: You have to refill before watering each plant.
Steps needed = 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 + 6 + 6 + 7 = 49.



풀이방법
- 화분별로 물을 써야 하는 누적합과, 해당 화분까지 가는데 걸리는 걸음수를 저장하는 배열을 만든다
- 이후 재귀로 다음 단계를 순환한다
  - 어디까지 물을 줄 수 있는지 구한다
    - 마지막 화분까지 물을 줄 수 있을경우 해당 화분까지 걸음수를 더한 뒤 재귀를 종료한다
    - 중간에 끊길경우 끊기는 지점까지의 걸음수 * 2를 더한다
    - 남는 화분의 물 누적합에 현재 소모한 물의 양을 빼고 재귀를 반복한다
*/

object Solution {
  def wateringPlants(plants: Array[Int], capacity: Int): Int = {

    def recurFunc(waterWithStep: Array[(Int, Int)], capacity: Int, res: Int): Int = {
      //println("-------------------------------------------")
      //println("waterWithStep: " + waterWithStep.mkString(","))
      //println("res: " + res)
      if(waterWithStep.isEmpty)
        res
      else {
        val remained = waterWithStep.filter(_._1 > capacity)
        val watered = waterWithStep.filter(_._1 <= capacity).maxBy(_._1)

        if(remained.isEmpty) {
          //println("step: " + waterWithStep.last._2)
          res + waterWithStep.last._2
        } else {
          //println("step: " + watered._2 * 2)
          recurFunc(waterWithStep.map(x => (x._1 - watered._1, x._2)).filter(_._1 > 0), capacity, res + watered._2 * 2)
        }
      }
    }

    def getWaterWithStep(plants: Array[Int], waterWithStep: Array[(Int, Int)], step: Int): Array[(Int, Int)] = {
      if(plants.isEmpty)
        waterWithStep
      else {
        val newWaterWithStep = waterWithStep ++ Array((if(waterWithStep.isEmpty) plants(0) else waterWithStep.last._1 + plants(0), step))

        getWaterWithStep(plants.drop(1), newWaterWithStep, step + 1)
      }
    }

    val waterWithStep = getWaterWithStep(plants, Array[(Int, Int)](), 1)
    //println("waterWithStep: " + waterWithStep.mkString(","))
    recurFunc(waterWithStep ,capacity, 0)
  }
}
