# TestPlatform
cmd登录
mysql -u root -p
123456
show databases;
show global variables like 'port';

创建数据库
create database TestPlatform character set utf8;

创建新的App时候用
python manage.py startapp xxxx

同步数据
python manage.py makemigrations
python manage.py migrate

创建后台admin账号
python manage.py createsuperuser
账号：admin  密码：admin123456

启动站点服务
python manage.py runserver 3002
python manage.py runserver 10.40.4.114:3002

python manage.py rundirect ./service/schedTask.py
python E:\GitHub\TestPlatform\manage.py rundirect E:\GitHub\TestPlatform\service\schedTask.py

官方资料
http://python.usyiyi.cn/translate/Django_111/index.html
https://docs.djangoproject.com/en/2.0/intro/tutorial01/