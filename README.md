<h1 align="center">
    <a href="https://github.com/Untouchable17/Real-Estate">
        <img src="https://i.ibb.co/k4Kqmv6/2023-02-02-14-50-15.png" width="700">
    </a>
</h1>

<h4 align="center"> The one stop shop for all matters properties. Buy, Rent or sell with us! </h4>

<p align="center">
<a href="https://github.com/Untouchable17/Real-Estate"><img src="https://img.shields.io/static/v1?label=version&message=1.0.7&color=blue"></a>
<a href="https://github.com/Untouchable17/Real-Estate/issues?q=is:issue+is:closed"><img src="https://img.shields.io/github/issues-closed/Untouchable17/Real-Estate?color=orange"></a>

</p>

# ESTATE WEBSITE

A website for searching for real estate, renting, as well as the opportunity to use the services of a realtor. The following technologies were used

1. Django
2. Django REST Framework
3. Djoser / PyJWT
4. Redis
5. Celery
6. Faker
7. Docker
8. React
9. Redux
10. PostgresSQL
11. NGINX



# Documentation

Installing and using Real Estate is very easy. Installation process:

1. Downloading or cloning this github repository.
2. Installing all dependencies.
3. Setting up the .env file.
4. Start Makefile




### Setting up the environment

Step 1 - Cloning the repository on your os system.

Below is the command which you can use in order to clone this repository.
```
git clone https://github.com/Untouchable17/Real-Estate
```

Step 2 - Make sure python3 and python3-pip is installed on your system.

You can also perform a check by typing this command in your terminal.
```
sudo apt install python3 python3-pip
```

Step 3 - Installing all dependencies for Django

Once you clone and check python installation, you will find directory name as **Real-Estate**. Just go to that directory and install using these commands:
```
cd Real-Estate
sudo pip3 install -r requirements.txt
```

Step 4 - Installing all dependencies for React
```
cd frontend
npm install package.json 
```

Step 4 - Setting up the enviroment file.

**Configure ENV - File**

```
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
CORS_ORIGIN_WHITELIST=

#DATABASE
POSTGRES_ENGINE=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
PG_HOST=
PG_PORT=

#LOGS
LOGS_PATH=
LOG_FILENAME=

#TOKENS SIGNATURE
SIGNING_KEY=

#EMAIL
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

DOMAIN=

CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
CELERY_ACCEPT_CONTENT=
CELERY_TASK_SERIALIZER=
CELERY_RESULT_SERIALIZER=
CELERY_BEAT_SCHEDULER=
CELERY_TIMEZONE=

```

> Warning: You must have Redis and PostgreSQL pre-installed

* Redis - https://redis.io/
* PostgreSQL - https://www.postgresql.org/download/

# Usage

Make migrations and migrate to database
```
python3 manage.py makemigrations
python3 manage.py migrate
```

**Tests**

Run PyTests before starting the django server
```
pytest
```

**Create superuser**

```
python3 manage.py createsuperuser
```

**Start django server**

```
python3 manage.py runserver
```

**Start redis server**
```
redis-server
```

**Start celery**

```
celery -A config worker -l info --beat
```


**Start react server**
```
npm start
```




# Start production server

If you need to run the application in production mode, run the following command

```
make -f Makefile 
```


# Contact Developer


    Telegram:           @secdet17
    Email:              tylerblackout17@gmail.com

