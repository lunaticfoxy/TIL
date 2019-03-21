"""
주소: https://leetcode.com/problems/odd-even-linked-list/

난이도: Medium

문제 내용
- 단방향 linked list가 주어졌을때 홀수번째 값들을 앞으로, 짝수번째 값들을 뒤로 밀어라

샘플
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

풀이 설명
- 3개의 포인터를 만듬
  - oddLast: 홀수번째 인덱스 집합의 맨 뒤를 가리킴
  - evenLast: 짝수번째 인덱스 집합의 맨 뒤를 가리킴
  - remainFirst: 아직 정리 안된 집합의 맨 앞을 가리킴
- 루프마다 일어나는 일
  - remainFirst를 evenLast의 다음 값으로 갱신
  - evenLast를 remainFirst 다음 값으로 갱신
  - oddLast 뒤에 remainFirst를 끼워넣음
- 종료조건
  - evenLast가 비어있을때
  - evenLast의 다음값이 비어있을때
- 엣지 케이스: 리스트 길이가 1 이하일때 (oddLast와 evenLast의 초기화가 불가능)

어떤 경우에 활용 가능할까
- 인덱스 정렬이야 사실 기본 언어에 있는걸 쓰면 됨
- 중요한건 2개의 포인터가 동시에 돌면서 처리한다는 점
- 따지고 보면 홀수-짝수 연산이 다른 모든 리스트에 적용하는 것과 동일한 방법 (세부 구현만 다름)
"""

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head
        
        oddLast = head
        evenLast = head.next
        remainFirst = head
        
        while evenLast and evenLast.next:
            remainFirst = evenLast.next
            evenLast.next = remainFirst.next
            remainFirst.next = oddLast.next
            oddLast.next = remainFirst
            oddLast = remainFirst
            evenLast = evenLast.next
            
        return head
