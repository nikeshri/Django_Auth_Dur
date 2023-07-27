# Django_Auth_Dur

![nik1](https://github.com/nikeshri/Django_Auth_Dur/assets/85691780/d3ec3f8b-9bff-4f7e-bcdc-52e473fe211f)
We have have register user by instering following name , email,phone and password and password is hashed by sha-56.


![nik2](https://github.com/nikeshri/Django_Auth_Dur/assets/85691780/45ae2f7f-db53-4322-8049-97044289401b)
Token is stored after the login is successful.


![nik3](https://github.com/nikeshri/Django_Auth_Dur/assets/85691780/1fac48c2-eb45-4344-9eef-a5d55f4f8444)
If password or username is incorrect.

![nik4](https://github.com/nikeshri/Django_Auth_Dur/assets/85691780/6f224594-0db6-4f00-b3b6-3b4314f452e5)
Logout successfulll.


for running
 1.pip install -r requiremnet.txt


for creating database set your database name in the setting.py

for refreshing or loading
 1.python manage.py makemigrations 
 2.python manage.py migrate

http://localhost:8000/api/register for register
http://localhost:8000/api/login for login
http://localhost:8000/api/logout for logut
http://localhost:8000/api/user for viewing a user





