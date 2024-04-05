# <span style="color:skyBlue"> Notion Job Application </span>
```
😜자소설 닷컴 캘린더를 내 노션에 넣기!
```

## ⚠ Notion Necessaries

+ DataBase
    - 노션에 API 를 받을 DB 를 생성
+ Column Setting
    - 데이터베이스의 Attribute 를 그림과 같이 설정 (이름과 속성 주의)
    ![notiondb](./docs/notion%20column.PNG)
+ Notion_API
    - 연결관계에 들어가서 내 APi 를 발급 받은 뒤 데이터 베이스에 연결
    ![notionAPI](./docs/notion%20api.PNG)
+ Notion_DB_ID
    - 보기링크를 복사   
    - https://www.notion.so/['DB_ID']=a8d039200f0e4436a8e73a6da74520c9&pvs=4
    - DB_ID



## GitHub Necessaries
+ Settings    
    ![Githubsettings](./docs/github%20settings.PNG)
    1. Secrets and Variables  
    2. actions  
    3. Repository Secrets  
    - 위에서 발급받은 db_ID 와 API 링크를 위 그림처럼 추가
    - ❗ 이름 중요, New repository secret 을 눌러서 추가

+ GitHub Action
    - Run Python Code








