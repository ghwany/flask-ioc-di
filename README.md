# Flask-IoC-DI

**Python3 Flask Toy project**

Python Flask, IoC(Inversion of Control), DI(Dependency Injection)

<br>

# 준비하기

1. `config/` 경로에 FLASK_ENV 환경에 맞는 .env파일을 준비

```ini
# FLASK_ENV=production >> production.env
# APPILCATION
FLASK_ENV = "development"
DEBUG = True

# DATABASE
DBMS = "mysql"
# docker-compose MariaDB의 경우 docker-compose에 지정한 container name으로 DB_HOST 지정
DB_HOST = "mysql"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "password"
DB_NAME = "dev"

SQLALCHEMY_ECHO = True

TZ = "Asia/Seoul"
```

2. docker-compose에 지정한 MariaDB 사용할 경우 `./config/orm.env` 파일에 DB정보 입력 후 아래 명령 수행

```docker
docker-compose up -d mysql
ENV=orm python ./src/manage.py run db:migration
```

<br>

# 시작하기 - Development

```docker
ENV=development docker-compose up -d app
```

<br>

# 시작하기 - Production

```docker
ENV=production docker-compose up -d app
```
