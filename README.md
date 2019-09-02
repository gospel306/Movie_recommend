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

