# BigDataSub2 - BOSS조

기능확장 및 클러스터링 알고리즘구현



### 설치하기

- Backend 설치
  - /backend 디렉토리 진입 후, 다음 커맨드를 순차적으로 실행

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

- Frontend 설치
  - /frontend 디렉토리 진입 후, 다음 커맨드 실행

```
npm install
```

- Django admin 계정 생성
  - /backend 디렉토리 진입 후, 다음 커맨드 실행

```
python manage.py shell < create_admin.txt
```



### 실행하기

- Backend 서버 실행
  - /backend 디렉토리 진입 후, 다음 커맨드를 실행

```
python manage.py runserver
```

- Frontend 개발 서버 실행
  - /frontend 디렉토리 진입 후, 다음 커맨드를 실행

```
npm run serve
```



### 영화 추천 알고리즘 api

#### KNN 영화 추천 불러오기

1) 알고리즘 실행해서 DB에 저장 **(!시간 오래걸리니까 조심)**
http://127.0.0.1:8000/api/KNN/?exe=1

2) 해당 유저의 추천 영화
http://127.0.0.1:8000/api/KNN/?user_id={userid}

2-1) 리턴형식: movie는 항상 10개가 들어있음. (rating,movieid)형식
```json
[
    {
        "movie": "[(5.0, 3697), (5.0, 3527), (5.0, 3470), (5.0, 3444), (5.0, 3439), (5.0, 3404), (5.0, 3265), (5.0, 3200), (5.0, 2985), (5.0, 2632)]",
        "user_id": 2
    }
]
```



3) 해당 영화를 추천할만한 유저
http://127.0.0.1:8000/api/KNN/?movie_id={movieid}

3-1) 리턴형식: user는 항상 10개가 들어있음. (rating,userid)형식

```json
[
    {
        "user": "[(4.0, 4157), (3.0, 4423), (3.0, 4285), (3.0, 4162), (3.0, 4050), (3.0, 1466), (2.0, 4790), (2.0, 4262), (2.0, 2995), (1.0, 3406)]",
        "movie_id": 2
    }
]
```



#### MF 영화 추천 불러오기

1) 알고리즘 실행해서 DB에 저장 **(! 실행하면 다 날아가고 다시 기록하니까 조심)**
http://127.0.0.1:8000/api/MF/?exe=1

2) 추천 영화 목록(중복제거)
http://127.0.0.1:8000/api/MF/?user_id={userid}

2-1) 리턴 형식: 영화는 항상 10개가 들어있음
```json
[
    {
        "rating": "4.91",
        "movie_id": 2579
    },
    {
        "rating": "4.88",
        "movie_id": 2727
    },
    {
        "rating": "4.83",
        "movie_id": 684
    },
    {
        "rating": "4.79",
        "movie_id": 2441
    },
    {
        "rating": "4.74",
        "movie_id": 40
    },
    {
        "rating": "4.73",
        "movie_id": 2019
    },
    {
        "rating": "4.69",
        "movie_id": 2960
    },
    {
        "rating": "4.65",
        "movie_id": 923
    },
    {
        "rating": "4.63",
        "movie_id": 858
    },
    {
        "rating": "4.63",
        "movie_id": 3568
    }
]
```

