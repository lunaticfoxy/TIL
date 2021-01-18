### 개요
- 데이터에 변경 발생시 해당 데이터를 참조하고 있는 객체들에게 변경여부를 알려주기 위한 디자인 패턴
- 데이터 저장 객체 : 데이터 구독 객체 = 1 : N 관계


### 사용
- 데이터 객체와 뷰 객체를 분리하여 관리하고자 할때 사용
- 데이터 객체의 상태가 변경될 경우 뷰의 갱신이 자동으로 일어나도록 하는 과정에서 의존성을 최소화 하기 위해 


### 패턴 없이 사용하는 경우와의 비교
- 점수 목록과 최대 최소를 계속해서 받아보는 경우
  - DataSheetView와 MinMaxView를 각각 따로 등록해줘야 함
  - 매번 새로운 객체가 생길때마다 데이터 저장 클래스의 수정 필요
- 데이터 저장 클래스와 뷰 클래스의 연결관계가 
```java
/* 입력된 점수를 저장하는 클래스 */
public class ScoreRecord {
  private List<Integer> scores = new ArrayList<Integer>(); // 점수를 저장함
  private DataSheetView dataSheetView; // 목록 형태로 점수를 출력하는 클래스
  private MinMaxView minMaxView; // 최소/최대 값만을 출력하는 형태의 클래스
  // DataSheetView를 설정함
  public void setDataSheetView(DataSheetView dataSheetView) { this.dataSheetView = dataSheetView; }
  // MinMaxView를 설정함
  public void setMinMaxView(MinMaxView minMaxView) { this.minMaxView = minMaxView; }
  // 새로운 점수를 추가하면 출력하는 것에 변화를 통보(update())하여 출력하는 부분 갱신
  public void addScore(int score) {
 scores.add(score); // scores 목록에 주어진 점수를 추가함
 dataSheetView.update(); // scores가 변경됨을 통보함
 minMaxView.update(); // scores가 변경됨을 통보함
  }
  // 출력하는 부분에서 변화된 내용을 얻어감
  public List<Integer> getScoreRecord() {
 return scores;
  }
}


/* 1. 출력형태: 목록 형태로 출력하는 클래스 */
public class DataSheetView {
  private ScoreRecord scoreRecord;
  private int viewCount;

  public DataSheetView(ScoreRecord scoreRecord, int viewCount) {
    this.scoreRecord = scoreRecord;
    this.viewCount = viewCount;
  }

  // 점수의 변경을 통보받음
  public void update() {
    List<Integer> record = scoreRecord.getScoreRecord(); // 점수를 조회함
    displayScores(record, viewCount); // 조회된 점수를 viewCount 만큼만 출력함
  }

  private void displayScores(List<Integer> record, int viewCount) {
    System.out.println("List of " + viewCount + " entries: ");
    for (int i = 0; i < viewCount && i < record.size(); i++) {
      System.out.println(record.get(i) + " ");
    }
    System.out.println();
  }
}


/* 2. 출력형태: 최소/최대 값만을 출력하는 형태의 클래스 */
public class MinMaxView {
  private ScoreRecord scoreRecord;
  // getScoreRecord()를 호출하기 위해 ScoreRecord 객체를 인자로 받음
  public MinMaxView(ScoreRecord scoreRecord) {
   this.scoreRecord = scoreRecord;
  }
  // 점수의 변경을 통보받음
  public void update() {
   List<Integer> record = scoreRecord.getScoreRecord(); // 점수를 조회함
   displayScores(record); // 최소값과 최대값을 출력함
  }
  // 최소값과 최대값을 출력함
  private void displayScores(List<Integer> record) {
   int min = Collections.min(record, null);
   int max = Collections.max(record, null);
   System.out.println("Min: " + min + ", Max: " + max);
  }
}

/* 실행이 일어나는 클라이언트 클래스 */
public class Client {
  public static void main(String[] args) {
   ScoreRecord scoreRecord = new ScoreRecord();
   // 3개까지의 점수만 출력함
   DataSheetView dataSheetView = new DataSheetView(scoreRecord, 3);
   // 최대값, 최소값만 출력함
   MinMaxView minMaxView = new MinMaxView(scoreRecord);
   // 각 통보 대상 클래스를 저장
   scoreRecord.setDataSheetView(dataSheetView);
   scoreRecord.setMinMaxView(minMaxView);
   // 10 20 30 40 50을 추가
   for (int index = 1; index <= 5; index++) {
     int score = index * 10;
     System.out.println("Adding " + score);
     // 추가할 때마다 최대 3개의 점수 목록과 최대/최소값이 출력됨
     scoreRecord.addScore(score);
   }
  }
}
```

### Observer 패턴 적용방법
- 추상 클래스, 인터페이스 정의
  - 데이터를 받아볼 Observer 인터페이스 정의
  - 데이터를 저장하기 위한 Subject 추상 클래스 정의
    - List<Observer> observers : 자신의 데이터를 구독하고 있는 옵저버들 저장
    - void attatch(Observer observer) : 옵저버 등록
    - void detatch(Observer observer) : 옵저버 해제
    - void notifyObservers() : 옵저버들에게 데이터 갱신 알림

- 데이터 저장 클래스는 Subject를 상속받아 정의: ConcreateSubject라 부름
  - 데이터 저장공간 선언
  - 데이터를 갱신하기 위한 함수 정의 (set, update, etc ...)
    - 데이터 갱신시마다 notifyObservers 호출
  - 데이터를 전달하는 함수 정의 (get)

- 뷰 클래스는 Observer를 상속받아 정의: ConcreateObserver라 
  - 다른 부분은 구현 동일

- 뷰 클래스가 변경되더라도 Subject 클래스에서는 알 필요 없음
  - 동일한 Observer 객체로 
```java
/* 추상화된 통보 대상 */
public interface Observer {
  // 데이터 변경을 통보했을 때 처리하는 메서드
  public abstract void update();
}

/* 추상화된 변경 관심 대상 데이터 */
// 즉, 데이터에 공통적으로 들어가야하는 메서드들 -> 일반화
public abstract class Subject {
  // 추상화된 통보 대상 목록 (즉, 출력 형태에 대한 Observer)
  private List<Observer> observers = new ArrayList<Observer>();

  // 통보 대상(Observer) 추가
  public void attach(Observer observer) { observers.add(observer);}
  // 통보 대상(Observer) 제거
  public void detach(Observer observer) { observers.remove(observer);}
  // 각 통보 대상(Observer)에 변경을 통보. (List<Observer>객체들의 update를 호출)
  public void notifyObservers() {
      for (Observer o : observers) {
          o.update();
      }
  }
}

/* 구체적인 변경 감시 대상 데이터 */
// 출력형태 2개를 가질 때
public class ScoreRecord extends Subject{
  private List<Integer> scores = new ArrayList<Integer>(); // 점수를 저장함
  // 새로운 점수를 추가 (상태 변경)
  public void addScore(int score) {
      scores.add(score); // scores 목록에 주어진 점수를 추가함
      notifyObservers(); // scores가 변경됨을 각 통보 대상(Observer)에게 통보함
  }
  public List<Integer> getScoreRecord() { return scores; }
}


/* 1. 출력형태: 목록 형태로 출력하는 클래스 */
public class DataSheetView implements Observer {
  private ScoreRecord scoreRecord;
  private int viewCount;

  public DataSheetView(ScoreRecord scoreRecord, int viewCount) {
    this.scoreRecord = scoreRecord;
    this.viewCount = viewCount;
  }

  // 점수의 변경을 통보받음
  public void update() {
    List<Integer> record = scoreRecord.getScoreRecord(); // 점수를 조회함
    displayScores(record, viewCount); // 조회된 점수를 viewCount 만큼만 출력함
  }

  private void displayScores(List<Integer> record, int viewCount) {
    System.out.println("List of " + viewCount + " entries: ");
    for (int i = 0; i < viewCount && i < record.size(); i++) {
      System.out.println(record.get(i) + " ");
    }
    System.out.println();
  }
}


/* 2. 출력형태: 최소/최대 값만을 출력하는 형태의 클래스 */
public class MinMaxView implements Observer {
  private ScoreRecord scoreRecord;
  // getScoreRecord()를 호출하기 위해 ScoreRecord 객체를 인자로 받음
  public MinMaxView(ScoreRecord scoreRecord) {
   this.scoreRecord = scoreRecord;
  }
  // 점수의 변경을 통보받음
  public void update() {
   List<Integer> record = scoreRecord.getScoreRecord(); // 점수를 조회함
   displayScores(record); // 최소값과 최대값을 출력함
  }
  // 최소값과 최대값을 출력함
  private void displayScores(List<Integer> record) {
   int min = Collections.min(record, null);
   int max = Collections.max(record, null);
   System.out.println("Min: " + min + ", Max: " + max);
  }
}

/* 실행이 일어나는 클라이언트 클래스 */
public class Client {
  public static void main(String[] args) {
      ScoreRecord scoreRecord = new ScoreRecord();

      // 3개까지의 점수만 출력함
      DataSheetView dataSheetView = new DataSheetView(scoreRecord, 3);
      // 최대값, 최소값만 출력함
      MinMaxView minMaxView = new MinMaxView(scoreRecord);

      // 각 통보 대상 클래스를 Observer로 추가
      scoreRecord.attach(dataSheetView);
      scoreRecord.attach(minMaxView);

      // 10 20 30 40 50을 추가
      for (int index = 1; index <= 5; index++) {
          int score = index * 10;
          System.out.println("Adding " + score);
          // 추가할 때마다 최대 3개의 점수 목록과 최대/최소값이 출력됨
          scoreRecord.addScore(score);
      }
  }
}
```


