### 개요
- MVP, MVVM 등의 패턴에서 Model과 Presentor / View Model 사이의 관계를 느슨하게 만들기 위해 사용
- 데이터 소스를 캡슐화하여 새로운 데이터 소스가 추가되더라도 Presenter / View Model 등의 수정이 불필요

### 필요성
- ViewModel에서 직접 데이터베이스에 접근하는 예제
- 문제점
  - 데이터베이스가 변경되면 ViewModel도 모두 변경 필요
  - ViewModel이 데이터베이스의 구조를 알아야 함
  - 비즈니스 로직 이외에 데이터베이스 연결 초기화 및 연결 해제를 위한 로직 존재

```kotlin
open class MainViewModels : ViewModel() {
  private val mRealm: Realm by lazy {
    Realm.getDefaultInstance()               // 데이터베이스 연결
  }
  
  fun getAllStudentData(): LiveData<RealmResults<Student>> {
    return mRealm.studentDao().getAllStudents()
  }
  
  fun insertStudent(student: Student) {
    mRealm.studentDao().insert(studnet)
  }
  
  override fun onCleared() {
    mRealm.close()                            // 데이터베이스 연결 해제
    super.onCleared()
  }
}
```

### 패턴 적용
- TestRepository를 ViewModel과 데이터베이스 사이에 두고 이를 통해 데이터 전달
```kotlin
class TestRepository {
  private val mRealm: Realm by lazy {
    Realm.getDefaultInstance()
  }
  
  fun getallStudentData(): LiveData<RealmResults<Student>> {
    return mRealm.studentDao().getAllStudents()
  }
  
  fun insert(student: Student) {
    return mRealm.studentDao().addStudent(student)
  }
}


open class MainViewModels : ViewModel() {
  private val mRepository: TestRepository by lazy {
    TestRepository()
  }
  
  fun getAllStudentData(): LiveData<RealmResults<Student>> {
    return mRepository.getAllStudentData()
  }
  
  fun insertStudent(student: Student) {
    mRepository.insert(studnet)
  }
}
```
