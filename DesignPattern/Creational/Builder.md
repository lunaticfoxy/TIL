### 개요
- 객체를 생성하기 위한 빌더 클래스를 별도로 정의하고, 이 빌더를 통해 실제 객체를 생성하는 방법
- 팩토리 매소드, 추상 팩토리 패턴과의 비교
  - 공통점
    - 직접 객체를 생성하지 않고 다른 클래스에 객체 생성을 위임함
  - 차이점
    - 팩토리
      - 팩토리 내의 메소드 호출이 발생하면 바로 객체 생성
      - 모든 파라미터를 한번에 전달
      - 하나의 팩토리에서 서로 다른 값을 포함하는 다수의 객체 생성
    - 빌더
      - 빌더 내의 메소드 중 객체를 생성하는 메소드와 값을 설정하는 메소드가 별도로 존재
      - 파라미터를 나누어 전달
      - 빌더의 상태가 동일하다면 생성되는 객체도 같은 값을 포함


### 필요성
- 개인의 정보를 저장하는 클래스 생성 예제
- 문제점
  - 일부의 정보만 포함하고 싶을 경우에 파라미터로 null 전달 필요
  - 생성자에 입력할 파라미터가 늘어나면 데이터 입력 순서 혼동 가능성 증가

```java
/**
 * 제약사항 : 이 객체는 한번 생성되면 읽기(Read)만 가능해야 합니다.
 */
public class PersonInfo {
    private String name;
    private Integer age;
    private String favoriteColor;
    private String favoriteAnimal;
    private Integer favoriteNumber;

    public PersonInfo(String name, Integer age, String favoriteColor, String favoriteAnimal, Integer favoriteNumber){
        this.name = name;
        this.age = age;
        this.favoriteColor = favoriteColor;
        this.favoriteAnimal = favoriteAnimal;
        this.favoriteNumber = favoriteNumber;
    }

    public String getName() {
        return name;
    }

    public Integer getAge() {
        return age;
    }

    public String getFavoriteColor() {
        return favoriteColor;
    }

    public String getFavoriteAnimal() {
        return favoriteAnimal;
    }

    public Integer getFavoriteNumber() {
        return favoriteNumber;
    }

    public String getPersonInfo(){
        String personInfo = String.format("name:%s, age:%d, favoriteColor:%s, favoriteAnimal:%s, favoriteNumber:%d"
                , name, age, favoriteColor, favoriteAnimal, favoriteNumber);
        return personInfo;
    }
}

PersonInfo p1 = new PersonInfo("JDM", 20, null, null, null);
PersonInfo p2 = new PersonInfo("cat", 20, "JDM", null, null); // 잘못된 호출
```

### 적용 방법
- 방법 1. 별도의 빌더 클래스 정의
  - 해당 클래스를 만들기 위한 빌더 클래스를 별도로 정의하여 활용
  - 파라미터를 하나씩 지정하여 상태로 가지고있고, build() 함수를 호출하여 실제 생성하고자 하는 객체 리턴
  
```java
public class PersonInfoBuilder {
    private String name;
    private Integer age;
    private String favoriteColor;
    private String favoriteAnimal;
    private Integer favoriteNumber;

    public PersonInfoBuilder setName(String name) {
        this.name = name;
        return this;
    }

    public PersonInfoBuilder setAge(Integer age) {
        this.age = age;
        return this;
    }

    public PersonInfoBuilder setFavoriteColor(String favoriteColor) {
        this.favoriteColor = favoriteColor;
        return this;
    }

    public PersonInfoBuilder setFavoriteAnimal(String favoriteAnimal) {
        this.favoriteAnimal = favoriteAnimal;
        return this;
    }

    public PersonInfoBuilder setFavoriteNumber(Integer favoriteNumber) {
        this.favoriteNumber = favoriteNumber;
        return this;
    }

    public PersonInfo build(){
        PersonInfo personInfo = new PersonInfo(name, age, favoriteColor, favoriteAnimal, favoriteNumber);
        return personInfo;
    }
}

public class BuilderPattern {
    public static void main(String[] args) {
        // 빌더 객체를 하나 만듭니다.
        PersonInfoBuilder personInfoBuilder = new PersonInfoBuilder();
        // 빌더 객체에 원하는 데이터를 입력합니다. 순서는 상관 없습니다.
        PersonInfo result = personInfoBuilder
                .setName("MISTAKE")
                .setAge(20)
                .setFavoriteAnimal("cat")
                .setFavoriteColor("black")
                .setName("JDM") // 다시 같은 메소드를 호출한다면 나중에 호출한 값이 들어갑니다.
                .setFavoriteNumber(7)
                // 마지막에 .build() 메소드를 호출해서 최종적인 결과물을 만들어 반환합니다.
                .build();
        // print is "name:JDM, age:20, favoriteColor:black, favoriteAnimal:cat, favoriteNumber:7"
        System.out.println(result.getPersonInfo());
    }
}
```

- 방법 2. 빌더 객체를 정의하되 빌더를 static으로 클래스 내에 포함
```java
public class PersonInfo {
    // 빌더 클래스를 리턴하는 스태틱 메소드 포함
    public static PersonInfoBuilder Builder(){
        return new PersonInfoBuilder();
    }
    
    // 아래 생략
}

public class BuilderPattern {
    public static void main(String[] args) {
        // 클래스내에 있는 static Build 메소드를 호출하여 빌더 가져옴
        PersonInfo p = PersonInfo.Builder().setName("JDM").setAge(20).build();
        System.out.println(result.getPersonInfo());
    }
}
```
